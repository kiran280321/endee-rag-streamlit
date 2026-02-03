import streamlit as st
import sys
import os

# Always add project root and backend to path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKEND_PATH = os.path.join(PROJECT_ROOT, "backend")

sys.path.append(PROJECT_ROOT)
sys.path.append(BACKEND_PATH)

from rag import generate_answer

st.title("📄 Endee RAG Document Assistant")

question = st.text_input("Ask a question from documents:")

if st.button("Get Answer"):
    if question:
        with st.spinner("Searching using vector database..."):
            answer = generate_answer(question)
        st.success(answer)
    else:
        st.warning("Please enter a question")
