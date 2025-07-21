Persistent Memory Chatbot 🤖

A production-ready,LLM-powered chatbot that remembers long-term conversations using RAG (Retrieval-Augmented Generation) and integrates stylish UI,monitoring and scalable memory storage.
---

🚀 Features

✅ LLaMA / OpenAI GPT API backend

✅ Pinecone vector database for conversation memory

✅ Retrieval-Augmented Generation (RAG) pipeline

✅ Streamlit frontend with modern animated design

✅ OpenTelemetry tracing & monitoring

✅ Modular, scalable Python codebase

✅ Optional summarization to compress memory

✅ NSFW-ready architecture for safety layers

---

🛠️ Tech Stack

Backend: FastAPI, OpenAI API, SentenceTransformers, Pinecone, LangChain (optional)

Frontend: Streamlit, Custom CSS

Memory: Pinecone Vector Database

Monitoring: OpenTelemetry

LLMs: OpenAI GPT / LLaMA / Mistral

Optional: LangFuse, LangGraph



---

📦 File Structure

persistent_memory_chatbot/
├── app/                    # Backend API code
├── models/                 # LLM & summarizer modules
├── db/                     # Vector DB interfaces
├── frontend/               # Streamlit UI + CSS
├── monitoring/             # Tracing via OpenTelemetry
├── tests/                  # Unit tests (to be created)
├── requirements.txt
├── Dockerfile (optional)
├── README.md


---

⚙️ Setup Instructions

1. Clone Repo:
git clone https://github.com/your-username/persistent-memory-chatbot.git


2. Install Dependencies:
pip install -r requirements.txt


3. Configure API Keys:
Create a .env file in project root:

OPENAI_API_KEY=your-openai-api-key
VECTOR_DB_TYPE=pinecone
VECTOR_DB_INDEX=chatbot_memory


4. Run Backend API:
uvicorn app.main:app --reload


5. Run Frontend:
In a separate terminal:
streamlit run frontend/app.py

---

📊 Monitoring

Traces are logged via OpenTelemetry Console Exporter.

Extend to support Jaeger/Prometheus via monitoring/tracing.py.


---

🏆 Project Highlights

Persistent, evolving chatbot memory.

Elegant, modern UI for conversations.

Modular and production-scalable design.

Extendable with summarization, safety layers, or multi-agent architectures.



---

🤝 Contributing

1. Fork the repo


2. Create your feature branch (git checkout -b feature/new-feature)


3. Commit changes (git commit -m 'Add new feature')


4. Push to branch (git push origin feature/new-feature)


5. Create a Pull Request




---

📄 License

MIT License © 2025 Robert Chonge
