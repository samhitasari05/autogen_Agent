import streamlit as st
import os
from dotenv import load_dotenv
from agents import ResearchAgent
from data_loader import DataLoader

print("ok")

# Streamlit UI Title
st.title("📚 Virtual Research Assistant")

# Retrieve the API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

# Check if API key is set, else stop execution
if not groq_api_key:
    st.error("GROQ_API_KEY is missing. Please set it in your environment variables.")
    st.stop()

# Initialize AI Agents for summarization and analysis
agents = ResearchAgent(groq_api_key)

# Initialize DataLoader for fetching research papers
data_loader = DataLoader()

# Input field for the user to enter a research topic
query = st.text_input("Enter a research topic:")
