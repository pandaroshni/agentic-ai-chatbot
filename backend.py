# Phase2-Setup Backend(With Fast API)
# 1.Setup Pydantic Model(Schema Validation)
from pydantic import BaseModel
from typing import List
import warnings
warnings.filterwarnings("ignore")

class RequestState(BaseModel):
    model_name:str
    model_provider:str
    system_prompt:str
    messages:List[str]
    allow_search:bool

# 2.Setup AI agent from frontend Request
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAMES=["llama3-70b-8192", "mixtral-8x7b-32768", "llama-3.3-70b-versatile", "gpt-4o-mini"]

app = FastAPI(title="Agentic AI Chatbot",debug=True)
@app.post("/chat")
def chat_endpoint(request:RequestState):
     """
    API Endpoint to interact with the Chatbot using LangGraph and search tools.
    It dynamically selects the model specified in the request
    """
     if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI model."}

     llm_id = request.model_name
     query=request.messages
     allow_search=request.allow_search
     system_prompt=request.system_prompt
     provider=request.model_provider



     # Create AI Agent and get response from it !!
     response=get_response_from_ai_agent(llm_id,query,allow_search,system_prompt,provider)

     return response


# 3.Run app and explore Swagger UI Docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)