from app.utils.embeddings import generate_embedding
from db.vector_db import store_vector

def store_message(user_id, message, response):
    for text in [message, response]:
        vector = generate_embedding(text)
        store_vector(user_id, text, vector)
