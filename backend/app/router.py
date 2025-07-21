from fastapi import APIRouter, Request
from app.utils.prompt_builder import build_prompt
from app.models.llm_wrapper import generate_response
from app.utils.memory import store_message
from app.utils.retriever import retrieve_memory

router = APIRouter()
@router.post("/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    user_id = data.get("user_id")
    message = data.get("message")

    history = retrieve_memory(user_id, message)
    prompt = build_prompt(history, message)
    response = generate_response(prompt)

    store_message(user_id, message, response)

    return {"response": response}

