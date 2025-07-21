import pinecone
from app.config import VECTOR_DB_INDEX, OPENAI_API_KEY

pinecone.init(api_key=OPENAI_API_KEY, environment="us-east1-gcp")
index = pinecone.Index(VECTOR_DB_INDEX)

def query_vector_db(user_id, query_vector, top_k=5):
    results = index.query(vector=query_vector.tolist(), top_k=top_k, include_metadata=True)
    return results.matches

def store_vector(user_id, text, vector):
    index.upsert([(f"{user_id}_{hash(text)}", vector.tolist(), {"text": text})])
