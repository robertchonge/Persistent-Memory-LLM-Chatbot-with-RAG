def build_prompt(history, message):
    context = "\n".join(history)
    return f"Conversation history:\n{context}\n\nUser: {message}\nAI:" 
