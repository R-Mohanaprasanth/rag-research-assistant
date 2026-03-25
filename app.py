import streamlit as st
from backend.ingest import extract_text
from backend.chunking import chunk_text
from backend.embeddings import embed_chunks
from backend.vectorstore import create_index
from backend.retriever import create_bm25
from backend.pipeline import rag_pipeline
import time

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Claude-style RAG", layout="wide")

# -------------------------------
# CUSTOM CSS (Claude Style)
# -------------------------------
st.markdown("""
<style>
.chat-container {
    max-width: 800px;
    margin: auto;
}

.user-msg {
    background-color: #2b2b2b;
    padding: 12px;
    border-radius: 10px;
    margin: 8px 0;
}

.bot-msg {
    background-color: #1f1f1f;
    padding: 12px;
    border-radius: 10px;
    margin: 8px 0;
}

.thinking {
    font-style: italic;
    color: #888;
}
</style>
""", unsafe_allow_html=True)

st.title("🧠 Research Assistant")
st.caption("Claude-style RAG Interface")

# -------------------------------
# SESSION STATE
# -------------------------------
if "history" not in st.session_state:
    st.session_state.history = []

if "chunks" not in st.session_state:
    st.session_state.chunks = None

if "index" not in st.session_state:
    st.session_state.index = None

if "bm25" not in st.session_state:
    st.session_state.bm25 = None

if "tokenized" not in st.session_state:
    st.session_state.tokenized = None

# -------------------------------
# FILE UPLOAD
# -------------------------------
uploaded_file = st.file_uploader("📄 Upload Research Paper")

@st.cache_resource
def process_pdf(file):
    with open("temp.pdf", "wb") as f:
        f.write(file.read())

    data = extract_text("temp.pdf")
    chunks = chunk_text(data)

    embeddings = embed_chunks(chunks)
    index = create_index(embeddings)

    bm25, tokenized = create_bm25(chunks)

    return chunks, index, bm25, tokenized


if uploaded_file:
    st.success("✅ Document Ready")

    chunks, index, bm25, tokenized = process_pdf(uploaded_file)

    st.session_state.chunks = chunks
    st.session_state.index = index
    st.session_state.bm25 = bm25
    st.session_state.tokenized = tokenized

# -------------------------------
# QUERY INPUT
# -------------------------------
query = st.chat_input("Ask anything about the paper...")

# -------------------------------
# HANDLE QUERY
# -------------------------------
if query and st.session_state.index is not None:

    # Show user message
    st.session_state.history.append(("user", query))

    # Show thinking animation
    thinking_placeholder = st.empty()
    thinking_placeholder.markdown(
        "<div class='thinking'>🧠 Thinking...</div>",
        unsafe_allow_html=True
    )

    # Simulate slight delay (Claude feel)
    time.sleep(1)

    ans, docs = rag_pipeline(
        query,
        st.session_state.index,
        st.session_state.chunks,
        st.session_state.bm25,
        st.session_state.tokenized
    )

    # Remove thinking
    thinking_placeholder.empty()

    # Save response
    st.session_state.history.append(("assistant", ans, docs))

# -------------------------------
# DISPLAY CHAT
# -------------------------------
for item in st.session_state.history:
    if item[0] == "user":
        st.markdown(
            f"<div class='user-msg'>🧑 {item[1]}</div>",
            unsafe_allow_html=True
        )

    elif item[0] == "assistant":
        st.markdown(
            f"<div class='bot-msg'>🤖 {item[1]}</div>",
            unsafe_allow_html=True
        )

        docs = item[2]

        # Sources (Claude-style expandable)
        with st.expander("🔍 Sources"):
            for d in docs:
                st.write(f"📄 Page {d['page']}")
                st.write(d["content"][:200] + "...")
                st.divider()