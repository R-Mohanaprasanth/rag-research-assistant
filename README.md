# 📚 Research Paper Explainer (Advanced RAG System)

## 🚀 Overview

This project is a **fully offline Research Paper Assistant** built using a **Retrieval-Augmented Generation (RAG)** pipeline.

It allows users to:

* Upload research papers (PDF)
* Ask natural language questions
* Get accurate, context-grounded answers with sources

The system combines **hybrid search, reranking, and a local LLM** to deliver high-quality responses without any external API dependency.

---

## 🎯 Key Highlights

* 🔍 Hybrid Retrieval (BM25 + Vector Search)
* 🔄 Cross-Encoder Reranking
* 🤖 Local LLM (Ollama - Llama3)
* 📄 PDF-based Question Answering
* 📌 Source Citation (Page-level)
* 💬 Claude-style Chat UI (Streamlit)
* ⚡ Cached Processing (fast performance)
* 🔒 Fully Offline & Privacy-Preserving
* 📊 Evaluation using RAGAS

---

## 🧠 Architecture

```
PDF → Text Extraction → Chunking → Embeddings → FAISS
                                      ↓
User Query → Hybrid Search → Reranking → LLM → Answer
```

---

## ⚙️ How It Works (Step-by-Step)

### 1. PDF Ingestion

* Extract text using PyMuPDF
* Preserve page metadata

### 2. Chunking

* Split text into smaller chunks
* Enables efficient retrieval

### 3. Embeddings

* Convert chunks into vectors using SentenceTransformers (BGE)
* Captures semantic meaning

### 4. Vector Storage

* Store embeddings in FAISS
* Enables fast similarity search

### 5. Hybrid Retrieval (Core Technique)

* BM25 → keyword-based search
* Vector search → semantic search
* Combine both for better accuracy

### 6. Reranking

* Cross-encoder model ranks retrieved chunks
* Improves relevance and precision

### 7. LLM Generation

* Uses Ollama (Llama3) locally
* Generates answers using retrieved context

### 8. Source Display

* Shows page number + snippet
* Improves transparency

---

## 🧠 Core Techniques Used

* Retrieval-Augmented Generation (RAG)
* Hybrid Search (BM25 + Dense Retrieval)
* Cross-Encoder Reranking
* Embedding-based Semantic Search
* Local LLM Inference (Ollama)
* RAG Evaluation (RAGAS)

---

## 🛠️ Tech Stack

| Component      | Tool                       |
| -------------- | -------------------------- |
| PDF Parsing    | PyMuPDF                    |
| Embeddings     | SentenceTransformers (BGE) |
| Vector DB      | FAISS                      |
| Keyword Search | Rank-BM25                  |
| Reranking      | CrossEncoder (BGE)         |
| LLM            | Ollama (Llama3)            |
| UI             | Streamlit                  |
| Evaluation     | RAGAS                      |

---

## 📁 Project Structure

```
research-rag/
│
├── app.py                  # Streamlit UI (Claude-style)
├── requirements.txt
│
├── backend/
│   ├── ingest.py          # PDF extraction
│   ├── chunking.py        # Text chunking
│   ├── embeddings.py      # Embedding generation
│   ├── vectorstore.py     # FAISS index
│   ├── retriever.py       # Hybrid retrieval
│   ├── reranker.py        # Reranking logic
│   ├── llm.py             # Ollama integration
│   └── pipeline.py        # Full RAG pipeline
│
├── evaluation/
│   ├── test_data.py
│   └── evaluate.py
│
├── data/
├── db/
└── README.md
```

---

## ⚡ Installation & Setup

### 1. Clone the Repository

```
git clone <your-repo-link>
cd research-rag
```

---

### 2. Install Dependencies

```
python -m pip install -r requirements.txt
```

---

### 3. Install Ollama

Download from:
https://ollama.com

---

### 4. Start Ollama

```
ollama serve
```

---

### 5. Download Model

```
ollama pull llama3
```

---

### 6. Run Application

```
streamlit run app.py
```

---

## 🧪 Usage

1. Upload a research paper (PDF)
2. Ask questions like:

   * “What is the main contribution?”
   * “Explain methodology”
   * “What are limitations?”
3. View answers + sources

---

## 🔒 Offline Capability

This system is **fully offline after setup**:

* No API calls
* No internet required
* Privacy-preserving

---

## 📊 Evaluation (RAGAS)

Metrics used:

* Context Precision
* Answer Relevance
* Faithfulness

---

## 🎨 UI Features

* ChatGPT / Claude-style interface
* Thinking indicator
* Chat history memory
* Expandable source view

---

## 🚀 Future Enhancements

* 📑 Multi-PDF comparison
* 🧠 Query rewriting (LLM-based)
* ⚡ Hybrid scoring (weighted fusion)
* 📊 Evaluation dashboard
* 🌐 Web deployment
* 🎤 Voice input support
* 🧾 Table & equation extraction
* 🔍 Section-aware retrieval

---

## 👨‍💻 Author

Mohanaprasanth R
B.Tech AI & Data Science Student

---
