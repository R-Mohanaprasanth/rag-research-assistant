# retriever.py
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer
import numpy as np

embed_model = SentenceTransformer('BAAI/bge-small-en')

def create_bm25(chunks):
    tokenized = [c["content"].split() for c in chunks]
    return BM25Okapi(tokenized), tokenized

def bm25_search(query, bm25, tokenized, chunks, k=5):
    scores = bm25.get_scores(query.split())
    top = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:k]
    return [chunks[i] for i in top]

def vector_search(query, index, chunks, k=5):
    emb = embed_model.encode([query])
    _, idx = index.search(np.array(emb), k)
    return [chunks[i] for i in idx[0]]

def hybrid_retrieve(query, index, chunks, bm25, tokenized, k=5):
    v = vector_search(query, index, chunks, k)
    b = bm25_search(query, bm25, tokenized, chunks, k)

    combined = v + b
    unique = {d["content"]: d for d in combined}.values()

    return list(unique)