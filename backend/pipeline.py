# pipeline.py
from backend.retriever import hybrid_retrieve
from backend.reranker import rerank
from backend.llm import generate_answer

def rag_pipeline(query, index, chunks, bm25, tokenized):

    docs = hybrid_retrieve(query, index, chunks, bm25, tokenized)
    ranked = rerank(query, docs)
    top_docs = ranked[:3]

    context = "\n".join([d["content"] for d in top_docs])
    answer = generate_answer(query, context)

    return answer, top_docs