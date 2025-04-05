from openai import OpenAI
from qdrant_client import QdrantClient

from ..utils.constants import init as init_constants

constants = init_constants()
openai_client = OpenAI(api_key=constants["OPENAI_API_KEY"])

def structure_embedding_text(interests, budget, type_of_tourism, transport_preference):
    return (
        f"Interests: {interests}\n"
        f"Budget: {budget}\n"
        f"Type of tourism: {type_of_tourism}\n"
        f"Transport preference: {transport_preference}"
    )

def generate_embedding(text):
    response = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=text,
        encoding_format="float"
    )
    return response.data[0].embedding

def query_similar_points(destination, interests, budget, type_of_tourism, transport_preference, service_types):
    qdrant_client = QdrantClient("localhost", port=constants["VECTORDB_PORT"])
    collection_name = constants["QDRANT_COLLECTION_NAME"]

    embedding_text = structure_embedding_text(interests, budget, type_of_tourism, transport_preference)
    embedding = generate_embedding(embedding_text)

    results = {}
    
    for service_type in service_types:
        query_filter = {
            "must": [
                {"key": "service_type", "match": {"value": service_type}},
                {"key": "location", "match": {"value": destination}}
            ]
        }

        if service_type == "HOTEL":
            limit=3
        else:
            limit=14

        # Execute the query
        response = qdrant_client.query_points(
            collection_name=collection_name,
            query=embedding,
            query_filter=query_filter,
            limit=limit,
        )

        # Collect the results
        results[service_type] = response

    return results

def generate_itinerary(destination, duration, transport_preference, type_of_tourism, budget, user_interests):
    service_types = ["HOTEL", "SERVICE"]

    developer_prompt = """
    Create a trip itinerary based on user-provided options in a fictional place. The itinerary should be detailed, taking into account the user's 
    preferences, available options, and any special instructions they may have provided. Return the itinerary in a well-structured JSON format.

    # Steps

    •⁠  ⁠Gather user inputs related to the trip, including destination, duration, interests, budget, and any specific preferences or constraints.
    •⁠  ⁠Utilize these inputs to research and decide on the best itinerary that aligns with the user's requirements.
    •⁠  ⁠Include key components in the itinerary, such as accommodation, activities, dining options, transportation details, and any unique experiences based on the provided preferences.
    •⁠  ⁠Consider the logical sequence of events to ensure a smooth and enjoyable trip.

    # Output Format

    The output should be a structured JSON object containing the following elements:

    ⁠ json
    {
    "destination": "string",
    "duration": "integer (number of days)",
    "budget": "string (e.g., 'moderate', 'luxury')",
    "itinerary": [
        {
        "day": "integer",
        "activities": [
            {
            "time": "string ('HH:MM AM/PM')",
            "activity": "string",
            "details": "string",
            "location": "string"
            }
        ]
        }
    ]
    }
     ⁠

    # Examples

    *User Input:*

    •⁠  ⁠Destination: Paris, France
    •⁠  ⁠Duration: 3 days
    •⁠  ⁠Interests: Museums, cuisine, shopping
    •⁠  ⁠Budget: Luxury

    *Example Output:*

    ⁠ json
    {
    "destination": "Paris, France",
    "duration": 3,
    "budget": "Luxury",
    "itinerary": [
        {
        "day": 1,
        "activities": [
            {
            "time": "09:00 AM",
            "activity": "Visit the Louvre Museum",
            "details": "Guided tour of the world's largest art museum.",
            "location": "Louvre Museum"
            },
            {
            "time": "01:00 PM",
            "activity": "Lunch at Le Meurice",
            "details": "Lunch at a 2-Michelin-star restaurant.",
            "location": "Le Meurice"
            },
            {
            "time": "03:00 PM",
            "activity": "Shopping on Champs-Elysées",
            "details": "Explore luxury brands and boutiques.",
            "location": "Champs-Elysées"
            }
        ]
        }
        // More days would follow in a similar structure
    ]
    }
     ⁠

    # Notes

    •⁠  ⁠Ensure that the itinerary is feasible within the time constraints.
    •⁠  ⁠Take into account travel time between activities and geographic locations.
    •⁠  ⁠Customize recommendations based on user-specified interests and budget considerations.
    •⁠  ⁠Be mindful of cultural norms or seasonal factors that may affect the itinerary.
    •⁠  ⁠Take into account the hotels and services that I have detected as most similar based on semantic search, including their reviews.
    •⁠  ⁠The answer must be in spanish

    """

    similar_points = query_similar_points(user_interests, service_types)


    user_prompt = f"""
    Destination: {destination}
    Duration: {duration} days
    Interests: {user_interests}
    Transport preference: {transport_preference}
    Type of tourism: {type_of_tourism}
    Budget: {budget}

    Here are some recommended hotels:
    {similar_points.get('HOTEL')}

    Here are some recommended services:
    {similar_points.get('SERVICE')}
    """

    completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "developer",
                "content": developer_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        response_format= { type: "json_object" }

    )

    return completion.choices[0].message.content