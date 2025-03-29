from openai import OpenAI
import pandas as pd
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, PointStruct
import math


openai_client = OpenAI(api_key="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")
qdrant_client = QdrantClient("localhost", port=6333)

collection_name = "Reviews"

# Read the Excel file
df = pd.read_csv("opiniones_turisticas.csv")

# Define a function to generate embeddings using OpenAI
def generate_embeddings(texts):
    response = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=texts,
        encoding_format="float"
    )
    
    print(len(response.data))
    
    return [embedding.embedding for embedding in response.data]

# Check if the collection exists, if not create one
if collection_name not in qdrant_client.get_collections().collections:
    qdrant_client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=1536, distance='Cosine')
    )

# Function to process in batches
def process_in_batches(df, batch_size=500):
    total_rows = len(df)
    num_batches = math.ceil(total_rows / batch_size)
    
    for batch_idx in range(num_batches):
        start_idx = batch_idx * batch_size
        end_idx = min(start_idx + batch_size, total_rows)
        batch_df = df.iloc[start_idx:end_idx]
        
        # Extract the 'comentario' column to send to OpenAI
        batch_texts = batch_df['comentario'].tolist()
        
        # Generate the embeddings for this batch
        embeddings = generate_embeddings(batch_texts)
        
        # Prepare batch points for Qdrant insertion
        points = []
        for idx, (embedding, row) in enumerate(zip(embeddings, batch_df.iterrows())):
            service_type = row[1]['tipo_servicio']
            review = row[1]['comentario']
            service_name = row[1]['nombre_servicio']
            payload = {'service_type': service_type, 'review': review, 'service_name': service_name}
            
            point = PointStruct(
                id=start_idx + idx,  # Unique ID based on the batch
                vector=embedding,  # The embedding vector
                payload=payload  # Store tipo_servicio and comentario
            )
            
            points.append(point)
        
        # Insert the batch into Qdrant
        qdrant_client.upsert(
            collection_name=collection_name,
            points=points
        )
        
        print(f"Processed batch {batch_idx + 1}/{num_batches}, from row {start_idx} to {end_idx - 1}")

# Process the CSV file in batches of 500
process_in_batches(df, batch_size=500)

print("Embeddings and payloads successfully inserted into Qdrant.")
