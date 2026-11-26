import streamlit as st
import os
from dotenv import load_dotenv
    
# Load environment variables
load_dotenv()

# langgraph and langchain imports
from langgraph.graph import StateGraph,START,END
from langgraph.graph import add_messages
from langgraph.checkpoint.memory import MemorySaver
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Annotated

