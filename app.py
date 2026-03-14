import streamlit as st
import ollama
import chromadb
from sentence_transformers import SentenceTransformer

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Knowledge Assistant",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# Title
# -----------------------------
st.title("🤖 Alfred.ai ")
st.markdown("### Welcome Batman! 🦇")
st.caption("Local RAG system powered by Ollama + ChromaDB")

# -----------------------------
# Initialize Models
# -----------------------------
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client()
collection = client.get_or_create_collection("rag_demo")

# -----------------------------
# Knowledge Base
# -----------------------------
documents = [

"Retrieval-Augmented Generation improves LLM responses by retrieving relevant documents before answering.",
"Vector databases store embeddings for semantic similarity search.",
"Embeddings convert text into numerical vectors representing meaning.",
"Agentic AI systems can reason, plan tasks, and use tools.",
"Ollama allows running large language models locally.",
"The average distance from Earth to the Moon is about 384,400 kilometers.",
"The speed of light is approximately 299,792 kilometers per second.",
"The human body contains 206 bones.",
"Mount Everest is the tallest mountain on Earth.",
"The Pacific Ocean is the largest ocean on Earth."

]

# Add docs only once
if collection.count() == 0:
    collection.add(
        documents=documents,
        ids=[f"doc{i}" for i in range(len(documents))]
    )

# -----------------------------
# Retrieval
# -----------------------------
def retrieve_docs(query):

    results = collection.query(
        query_texts=[query],
        n_results=2
    )

    return " ".join(results["documents"][0])

# -----------------------------
# LLM
# -----------------------------
def ask_llm(query, context):

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": f"Use this context to answer: {context}"},
            {"role": "user", "content": query}
        ]
    )

    return response["message"]["content"]

# -----------------------------
# Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# Chat Input
# -----------------------------
prompt = st.chat_input("Ask a question...")

if prompt:

    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Retrieve docs
    context = retrieve_docs(prompt)

    # LLM answer
    answer = ask_llm(prompt, context)

    with st.chat_message("assistant"):
        st.markdown(answer)

        with st.expander("📚 Retrieved Context"):
            st.write(context)

    st.session_state.messages.append({"role": "assistant", "content": answer})