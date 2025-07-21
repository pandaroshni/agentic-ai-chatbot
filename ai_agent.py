# Step 1.Setup API keys for groq ,Open AI and tavily

import os

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY=os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")

# Step 2.Setup LLM and tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_tavily import TavilySearch

openai_llm=ChatOpenAI(model="gpt-4o-mini")
groq_llm=ChatGroq(model="llama-3.3-70b-versatile")


search_tools=TavilySearch(max_results=2)


# Step 3. Setup AI agent with serach tool functionality

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage



def get_response_from_ai_agent(llm_id,query,allow_search,system_prompt,provider):
    system_prompt=("Act as an AI chatbot who is smart and friendly")
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm=ChatOpenAI(model=llm_id)

    tools=[TavilySearchResults(max_results=2)] if allow_search else []
    
    agent=create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt
    )


    state={"messages":query}
    response=agent.invoke(state)
    messages=response.get("messages")
    ai_message = [message.content for message in messages if isinstance(message, AIMessage)]
    return ai_message[-1]
