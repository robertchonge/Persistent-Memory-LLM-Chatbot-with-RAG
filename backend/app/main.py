from fastapi import FastAPI, Request
from app.router import router

app = FastAPI(title="Persistent Memory Chatbot")

app.include_router(router)

# Run with: uvicorn app.main:app --reload

