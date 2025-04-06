from openai import OpenAI
from qdrant_client import QdrantClient, models

from ..utils.constants import init as init_constants

constants = init_constants()
openai_client = OpenAI(api_key=constants["OPENAI_API_KEY"])

def structure_user_preferences(destination, destination_description, transport_preference, type_of_tourism, budget, user_interests):
    return (
        f"Destino: {destination}\n"
        f"Descripción del destino: {destination_description}"
        f"Preferencia de transporte: {transport_preference}"
        f"Type of tourism: {type_of_tourism}\n"
        f"Presupuesto: {budget}\n"
        f"Intereses del usuario: {user_interests}\n"
    )

def generate_embedding(text):
    response = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=text,
        encoding_format="float"
    )
    return response.data[0].embedding

def query_similar_points(destination, destination_description, transport_preference, type_of_tourism, budget, user_interests):
    qdrant_client = QdrantClient("localhost", port=constants["VECTORDB_PORT"])
    collection_name = constants["QDRANT_COLLECTION_NAME"]

    embedding_text = structure_user_preferences(destination, destination_description, transport_preference, type_of_tourism, budget, user_interests)
    embedding = generate_embedding(embedding_text)

    results = {}
    service_types = ["HOTEL", "SERVICIO"]

    
    for service_type in service_types:
        if service_type == "HOTEL":
            limit=3
        else:
            limit=14

        if not qdrant_client.collection_exists(collection_name):
            raise ValueError(f"Collection '{collection_name}' does not exist.")

        response = qdrant_client.query_points(
            collection_name=collection_name,
            query=embedding,
            query_filter=models.Filter(
                must=[
                    models.FieldCondition(
                        key="location",
                        match=models.MatchValue(
                            value=destination,
                        ),
                    ),
                    models.FieldCondition(
                        key="service_type",
                        match=models.MatchValue(
                            value=service_type,
                        ),
                    ),
                ]
            ),
            limit=limit,
        )

        results[service_type] = response

    return results

def generate_itinerary(destination, destination_description, duration, transport_preference, type_of_tourism, budget, user_interests):
    developer_prompt = """
    Crea un itinerario de viaje basado en las opciones proporcionadas por el usuario en un lugar ficticio. El itinerario debe ser detallado, teniendo en cuenta las preferencias del usuario, las opciones disponibles y cualquier instrucción especial que haya proporcionado. Devuelve el itinerario en un formato JSON bien estructurado.

    # Pasos

    •⁠  ⁠Recopila los datos del usuario relacionados con el viaje, incluyendo destino, duración, intereses, presupuesto y cualquier preferencia o restricción específica.
    •⁠  ⁠Utiliza esta información para investigar y decidir el mejor itinerario que se ajuste a los requisitos del usuario.
    •⁠  ⁠Incluye componentes clave en el itinerario, como alojamiento, actividades, opciones gastronómicas, detalles de transporte y cualquier experiencia única basada en las preferencias proporcionadas.
    •⁠  ⁠Considera la secuencia lógica de los eventos para asegurar un viaje fluido y agradable.

    # Formato de salida

    La salida debe ser un objeto JSON estructurado que contenga los siguientes elementos:

    ⁠ json
    {
    "destination": "string",
    "duration": "integer (número de días)",
    "budget": "string (por ejemplo, 'moderado', 'lujo')",
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

    # Ejemplos

    *Entrada del usuario:*

    •⁠  ⁠Destino: París, Francia  
    •⁠  Descripción del destino: Ciudad histórica, con algunos de los merores restaurantes del mundo y exclusivas boutiques para hacer compras.
    •⁠  ⁠Duración: 3 días  
    •⁠  ⁠Intereses: Museos, gastronomía, compras  
    •⁠  Tipo de turismo: Gastronómico, Histórico
    •⁠  ⁠Presupuesto: Lujo  

    *Ejemplo de salida:*

    ⁠ json
    {
    "destination": "París, Francia",
    "duration": 3,
    "budget": "Lujo",
    "itinerary": [
        {
        "day": 1,
        "activities": [
            {
            "time": "09:00 AM",
            "activity": "Visita al Museo del Louvre",
            "details": "Visita guiada al museo de arte más grande del mundo.",
            "location": "Museo del Louvre"
            },
            {
            "time": "01:00 PM",
            "activity": "Almuerzo en Le Meurice",
            "details": "Almuerzo en un restaurante con 2 estrellas Michelin.",
            "location": "Le Meurice"
            },
            {
            "time": "03:00 PM",
            "activity": "Compras en los Campos Elíseos",
            "details": "Explora boutiques y marcas de lujo.",
            "location": "Campos Elíseos"
            }
        ]
        }
        // Más días seguirían en una estructura similar
    ]
    }

    # Notas

    •⁠  ⁠Asegúrate de que el itinerario sea factible dentro de las limitaciones de tiempo.
    •⁠  ⁠Ten en cuenta el tiempo de traslado entre actividades y ubicaciones geográficas.
    •⁠  ⁠Personaliza las recomendaciones según los intereses y el presupuesto especificados por el usuario.
    •⁠  ⁠Ten en cuenta los hoteles y servicios que he detectado como más similares mediante búsqueda semántica, incluyendo sus reseñas.
    """

    similar_points = query_similar_points(destination, destination_description, transport_preference, type_of_tourism, budget, user_interests)

    user_prompt = f"""
    Destino: {destination}
    Descripción del destino: {destination_description}
    Duración: {duration} days
    Intereses del usuario: {user_interests}
    Preferencia de transporte: {transport_preference}
    Tipo de turismo: {type_of_tourism}
    Presupuesto: {budget}

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
    )

    print(completion.choices[0].message.content)

    return completion.choices[0].message.content