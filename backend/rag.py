from search import semantic_search

def generate_answer(question):
    """
    RAG-style answer generation without LLM.
    Retrieves relevant document chunks using vector search (Endee)
    and returns them as the answer.
    """
    retrieved_chunks = semantic_search(question)

    if not retrieved_chunks:
        return "No relevant information found."

    answer = " ".join(retrieved_chunks)
    return answer
