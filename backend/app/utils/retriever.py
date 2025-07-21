from app.utils.embeddings import generate_embedding
from db.vector_db import query_vector_db


def retrieve_memory(user_id, message, top_k=5):
    query_vector = generate_embedding(message)
    results = query_vector_db(user_id, query_vector, top_k)
    return [item["text"] for item in results]
