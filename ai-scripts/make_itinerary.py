from openai import OpenAI
from qdrant_client import QdrantClient
import numpy as np
import os
from pydantic import BaseModel

openai_client = OpenAI(api_key="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")
qdrant_client = QdrantClient("localhost", port=6333)

collection_name = "Reviews"

class KeyConceptsExtraction(BaseModel):
    key_concepts_hotels: list[str]
    key_concepts_routes: list[str]
    key_concepts_services: list[str]
    

# Function to get key concepts from GPT-4 for each service
def get_key_concepts(user_message):
    
    # GPT-4 call to generate key concepts
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "developer", "content": "You are a pre-processing step for a AI powered trip planner. You must extract the key words which should be used to generate embeddings in a semantic search."},
            {"role": "user", "content": "extract the key concepts for this review: ¡¡¡WOW!!! ¡¡¡QUÉ EXPERIENCIA INCREÍBLE EN EL APOLLO EXECUTIVE BEACH RESORT!!! ¡¡¡ES SIN DUDA EL MEJOR HOTEL EN EL QUE ME HE HOSPEDADO!!! 💯🌟 ¡La DECORACIÓN es simplemente ESPECTACULAR!!! 🎨✨ Desde el momento en que entras te sientes como en un sueño: techos altos lámparas modernas muebles de diseño y detalles que combinan elegancia y comodidad. ¡Las habitaciones son un PARAÍSO!!! 🏝️ La cama era TAN CÓMODA que no quería levantarme y la vista al mar desde el balcón era simplemente INCREÍBLE. ¡El baño tenía una bañera de lujo y productos de cuidado personal de PRIMERA CALIDAD! 🛁🧴 ¡Las AMENIDADES son DE OTRO MUNDO!!! 🌍✨ La piscina infinita con vista al océano es algo que nunca olvidaré. ¡El gimnasio está totalmente equipado y el spa es RELAJACIÓN PURA!!! 💆\u200d♀️💆\u200d♂️ Además tienen actividades diarias como yoga al amanecer y clases de cocina. ¡El personal es SUPER AMABLE y siempre,"},
            {"role": "assistant",
                "content": """Experiencia increíble en el Apollo Executive Beach Resort.
                            Decoración espectacular, combinando elegancia y comodidad.
                            Habitaciones cómodas, con vista al mar y cama acogedora.
                            Amenidades de lujo, incluyendo baño con productos de alta calidad.
                            Instalaciones excepcionales: piscina infinita, gimnasio completo, y spa.
                            Actividades diarias como yoga al amanecer y clases de cocina.
                            Personal amable y servicial."""
            },
            {"role": "user", "content": f"Here is the user query: {user_message}"},
        ],
    )
    # Return the response as a list of key concepts (parse the text into a list of bullet points)
    concepts = response.choices[0].message.content
    return concepts

# Function to generate embedding using OpenAI's text-embedding-ada-003 model
def generate_embedding(text: str):
    response = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=text,
        encoding_format="float"
    )
    # Extracting the embedding from the response
    return response.data[0].embedding

# Define the function that queries Qdrant
def query_similar_points(text: str, service_types):
    # Generate the embedding for the input text
    embedding = generate_embedding(text)

    # Perform three queries with the same embedding but different parameters
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
            collection_name=collection_name,  # Name of your Qdrant collection
            query=embedding,
            query_filter=query_filter,
            limit=5,  # Limit the number of results returned
        )

        # Collect the results
        results.append(response)

    return results

# Example usage of the function
if __name__ == "__main__":
    text = "Quiero vistas al mar."
    key_concepts = get_key_concepts(text)
    print(key_concepts)
    service_types = ["Ruta", "Servicio", "Hotel"]
    similar_points = query_similar_points(text, service_types)
    
    # Display results
    # for i, result in enumerate(similar_points):
    #     print(f"Query {i+1} Results:")
    #     for item in result:
    #         print(item)
    #     print("---------")