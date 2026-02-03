import streamlit as st
import sys
import os

BACKEND_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend"))
sys.path.append(BACKEND_PATH)

from rag import generate_answer

st.title("📄 Endee RAG Document Assistant")

question = st.text_input("Ask a question from documents:")

if st.button("Get Answer"):
    if question:
        with st.spinner("Searching & generating answer..."):
            answer = generate_answer(question)
        st.success(answer)
