# embeddings.py
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('BAAI/bge-small-en')

def embed_chunks(chunks):
    texts = [c["content"] for c in chunks]
    return model.encode(texts)