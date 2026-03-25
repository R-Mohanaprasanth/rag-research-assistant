# README.md
# 📚 Research Paper Explainer (Advanced RAG System)

A fully offline, production-style Retrieval-Augmented Generation (RAG) system that allows users to upload research papers and ask intelligent questions with source-grounded answers.

---

## 🚀 Features

- 📄 PDF Upload & Parsing
- ✂️ Smart Chunking with metadata
- 🧠 Semantic Search (FAISS + BGE embeddings)
- 🔎 Hybrid Search (BM25 + Vector Search)
- 🔄 Cross-Encoder Reranking
- 🤖 Local LLM (Ollama - Llama3/Mistral)
- 📌 Source Citation (page-level)
- 💬 Chat Interface (Streamlit)
- 📊 RAG Evaluation (RAGAS)

---

## 🧠 Architecture

User Query  
→ Hybrid Retrieval (BM25 + Vector)  
→ Reranking  
→ Context Selection  
→ Local LLM (Ollama)  
→ Answer + Sources  

---

## 💯 Fully Offline & Free

This project runs completely offline using local models:
- No OpenAI API
- No cloud dependency
- Privacy-preserving

---

## ⚙️ Tech Stack

- Python
- Streamlit
- PyMuPDF
- FAISS
- SentenceTransformers (BGE)
- Rank-BM25
- Ollama (Llama3)
- RAGAS

---

## 🛠️ Installation

```bash
pip install -r requirements.txt