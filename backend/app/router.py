from fastapi import APIRouter, Request
from app.utils.prompt_builder import build_prompt
from app.models.llm_wrapper import generate_response
from app.utils.memory import store_message
from app.utils.retriever import retrieve_memory

router = APIRouter()
