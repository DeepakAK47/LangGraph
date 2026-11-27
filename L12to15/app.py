import sqlite3
from langchain_core.messages import HumanMessage, AIMessage

import streamlit as st
import os
from dotenv import load_dotenv
    
# Load environment variables
load_dotenv()

# langgraph and langchain imports
from langgraph.graph import StateGraph,START,END
from langgraph.graph import add_messages
from langgraph.checkpoint.sqlite import SQLiteSaver # for adding memory
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Annotated # it is use use to combined the previous and current data because LangGraph by default used override concept


# State defination
class State(TypedDict):
    messages: Annotated[list[HumanMessage | AIMessage], "The list of messages in the conversation"]
    memory: Annotated[dict, "The memory of the conversation"]

# Initialize LLM 
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite", temperature=0.2,api_key=os.getenv("GOOGLE_API_KEY"))   

def chat_bot(state : State):
    response = llm.invoke(state["messages"])
    return {'messages':[response], 'memory': state['memory']}

# build the graph + sqlite persistence
builder = StateGraph(State)
builder.add_node("chat_bot", chat_bot,input_keys=["messages", "memory"],output_keys=["messages", "memory"],)  
builder.add_edge(START, "chat_bot")
builder.add_edge("chat_bot", END)

