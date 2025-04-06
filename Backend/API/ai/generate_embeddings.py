from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams
from openai import OpenAI
from uuid import uuid4

from ..dao.reviews import Reviews
from ..utils.constants import init as init_constants

constants = init_constants()

def generate_embeddings_batch(texts):
    openai_client = OpenAI(api_key=constants["OPENAI_API_KEY"])
    response = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=texts,
        encoding_format="float"
    ) 
    return [embedding.embedding for embedding in response.data]

def init_db_ai():
    qdrant_client = QdrantClient(constants["VECTORDB_HOST"], port=constants["VECTORDB_PORT"])
    collection_name = constants["QDRANT_COLLECTION_NAME"]

    if collection_name not in qdrant_client.get_collections().collections:
        qdrant_client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=1536, distance='Cosine')
        )

    reviews: Reviews = Reviews.get_all_rows()

    batch_size = constants["EMBEDDINGS_GENERATION_BATCH_SIZE"]

    for i in range(0, len(reviews), batch_size):
        batch_reviews = reviews[i:i + batch_size]
        batch_comments = [review.comment for review in batch_reviews]

        embeddings_batch = generate_embeddings_batch(batch_comments)

        points = []
        for embedding, review in zip(embeddings_batch, batch_reviews):
            review_text = review.comment
            if review.hotel_id is not None:
                service_type = "HOTEL"
                service_name = review.hotel.name
                service_location = review.hotel.city.name
            elif review.service_id is not None:
                service_type = "SERVICE"
                service_name = review.service.name
                service_location = review.service.city.name
            else:
                service_type = "UNKNOWN"
            
            payload = {
                'service_review': review_text,
                'service_type': service_type,
                'service_name': service_name,
                'location': service_location
            }

            point = PointStruct(
                id=str(uuid4()),
                vector=embedding,
                payload=payload
            )

            points.append(point)
        
        # Insert the batch into Qdrant
        qdrant_client.upsert(
            collection_name=collection_name,
            points=points
        )
    

