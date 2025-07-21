# Phase 3- Setup Frontend
# 1.setup UI with Streamlit (model provider,model ,system prompt, web serach, query)
import streamlit as st

st.set_page_config(page_title="Agentic AI Chatbot", page_icon=":robot_face:", layout="wide")
st.title("Agentic AI Chatbot ")
st.write("Interact with the chatbot using different AI models and search tools.")

system_prompt = st.text_area("Define Your AI Agent:", height=70 ,placeholder="Type your system prompt here...")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768","llama3-70b-8192"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

model_provider = st.radio("Select  Provider:", ["Groq", "OpenAI"])

if model_provider == "Groq":
    selected_model = st.selectbox("Select Model:", MODEL_NAMES_GROQ)
elif model_provider == "OpenAI":
    selected_model = st.selectbox("Select Model:", MODEL_NAMES_OPENAI)

allow_web_search = st.checkbox("Allow Web Search")
user_query = st.text_area("Enter Your Query:", height=150, placeholder="Ask your query here...")

API_URL="http://127.0.0.1:8000/chat"
if st.button("Ask Agent"):
    if user_query.strip():
        
# 2.Connect with backend via URL 
        import requests
        payload = {
            "model_name": selected_model,
            "model_provider": model_provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
        #get response from backend and show here
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data}")

