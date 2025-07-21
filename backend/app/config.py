import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
VECTOR_DB_TYPE = os.getenv("VECTOR_DB_TYPE", "pinecone")
VECTOR_DB_INDEX = os.getenv("VECTOR_DB_INDEX", "chatbot_memory")
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")
