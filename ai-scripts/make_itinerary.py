from openai import OpenAI
from qdrant_client import QdrantClient

openai_client = OpenAI(api_key="")
qdrant_client = QdrantClient("localhost", port=6333)

collection_name = "Reviews"

# Function to generate embedding using OpenAI's text-embedding-3-small
def generate_embedding(text: str):
    response = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=text,
        encoding_format="float"
    )
    return response.data[0].embedding

# Define the function that queries Qdrant
def query_similar_points(text: str, service_types):
    embedding = generate_embedding(text)

    results = []

    for service_type in service_types:
        # Query parameters (you can adjust the filter as needed)
        query_filter = {
            "must": [
                {"key": "service_type", "match": {"value": service_type}}  # Filtering by service_type
            ]
        }

        # Execute the query
        response = qdrant_client.query_points(
            collection_name=collection_name,
            query=embedding,
            query_filter=query_filter,
            limit=5,
        )

        # Collect the results
        results.append(response)

    return results

# Example usage of the function
if __name__ == "__main__":
    text = "Me gustaría hacer un viaje a la playa en el que el atardecer sea fantástico"
    service_types = ["Ruta", "Servicio", "Hotel"]
    similar_points = query_similar_points(text, service_types)
    
    for i, result in enumerate(similar_points):
        print(f"Query {i+1} Results:")
        for item in result:
            print(item)
        print("---------")