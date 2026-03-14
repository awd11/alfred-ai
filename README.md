# Alfred.ai 🤖

A local Retrieval-Augmented Generation (RAG) application built using **Ollama, ChromaDB, SentenceTransformers, and Streamlit**.

This project demonstrates how to build a lightweight AI assistant that retrieves knowledge from a vector database and generates answers using a local LLM.

---

## Features

- Local LLM inference using **Ollama (Llama3)**
- Semantic search with **ChromaDB**
- Embeddings using **SentenceTransformers**
- Retrieval-Augmented Generation pipeline
- Modern **Streamlit chat interface**
- Works fully **offline**

---

## Architecture

User Question  
↓  
Embedding  
↓  
Vector Search (ChromaDB)  
↓  
Retrieve Context  
↓  
LLM (Llama3 via Ollama)  
↓  
Generated Answer

---

## Tech Stack

- Python
- Streamlit
- Ollama
- ChromaDB
- SentenceTransformers
- LangGraph (for agent workflows)

---

## Installation

Clone the repository

```bash
git clone https://github.com/awd11/alfred-ai.git
cd alfred-ai