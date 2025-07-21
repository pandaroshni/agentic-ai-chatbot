# Agentic AI Chatbot
1.Overview
This project implements an end-to-end AI agent chatbot powered by LangGraph and LangChain, served via FastAPI, and optionally visualized through Streamlit. The chatbot supports multiple LLMs (e.g., Groq’s LLaMA‑3.3, Mixtral‑8x7b, OpenAI GPT‑4o‑mini) and can perform web searches using Tavily, providing intelligent, context-aware responses.

2. Features
Multi‑model support: Use Groq or OpenAI LLMs.

Tool-enabled agents: Incorporates search & custom toolkits via LangChain.

Web interface: Built with Streamlit for quick testing.

Production-ready: Backend powered by FastAPI (with Swagger UI).

Modular & scalable: LangGraph state-machine orchestration. Inspired by production templates.

3. Architecture
<img width="1077" height="641" alt="image" src="https://github.com/user-attachments/assets/6baa7f08-904b-466b-8bd6-be37f7ad731f" />


5. Installation & Environment Setup
   
1.Install dependencies:
pip install -r requirements.txt

2.Setup .env with:
OPENAI_API_KEY="your_api_key"
GROQ_API_KEY="your_api_key"
TAVILY_API_KEY="your_api_key"

7. Running the App
Backend (FastAPI)
uvicorn backend:app --reload --port 8000

Frontend (Streamlit)
streamlit run frontend.py

📁 Project Structure
Agentic-AI-Chatbot/
│
├── 📂 agents/
│   └── ai_agent.py              # Sets up LangGraph + LangChain agent with tools
│
├── 📂 backend/
│   └── main.py                  # FastAPI app (entry point for backend API)
│
├── 📂 frontend/
│   └── frontend.py              # Streamlit UI interacting with backend
│
├── .env                         # Environment variables (API keys.)
├── requirements.txt             # Python dependency list
├── README.md                    # Project documentation

