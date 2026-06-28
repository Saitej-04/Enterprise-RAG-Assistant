import streamlit as st

from src.pdf_loader import extract_text_from_pdfs
from src.text_splitter import split_text
from src.embeddings import get_embedding_model
from src.vector_store import create_vector_store
from src.retriever import get_retriever
from src.chat_model import get_chat_model
from src.rag_chain import get_answer

from src.memory import (
    initialize_memory,
    add_user_message,
    add_ai_message,
    get_messages,
    clear_chat
)

# ---------------------------------
# Page Config
# ---------------------------------

st.set_page_config(
    page_title="Enterprise Financial Intelligence Assistant",
    page_icon="📊",
    layout="wide"
)

initialize_memory()

# ---------------------------------
# Sidebar
# ---------------------------------

with st.sidebar:

    st.title("💬 Chat")
    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        clear_chat()
        st.rerun()

# ---------------------------------
# Main Title
# ---------------------------------

st.title("📊 Enterprise Financial Intelligence Assistant")
st.markdown("### 📄 Upload Financial Documents")

uploaded_files = st.file_uploader(
    "Choose PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)

# ---------------------------------
# Process PDFs
# ---------------------------------

if uploaded_files:

    try:

        st.success(f"✅ {len(uploaded_files)} PDF(s) Uploaded Successfully")

        for file in uploaded_files:
            st.write(
                f"📄 {file.name} ({round(file.size/1024,2)} KB)"
            )

        # ----------------------------
        # Extract Documents
        # ----------------------------

        documents = extract_text_from_pdfs(uploaded_files)
        st.success("✅ Documents Extracted")

        # ----------------------------
        # Split Documents
        # ----------------------------

        chunks = split_text(documents)
        st.success(f"✅ Total Chunks : {len(chunks)}")

        # ----------------------------
        # Embeddings
        # ----------------------------

        embedding_model = get_embedding_model()
        st.success("✅ Embedding Model Loaded")

        # ----------------------------
        # Vector Store
        # ----------------------------

        vector_store = create_vector_store(
            chunks,
            embedding_model
        )

        st.success("✅ Vector Store Created")

        # ----------------------------
        # Retriever
        # ----------------------------

        retriever = get_retriever(vector_store)
        st.success("✅ Retriever Ready")

        # ----------------------------
        # Gemini
        # ----------------------------

        llm = get_chat_model()
        st.success("✅ Gemini Model Loaded")

        st.success("✅ Enterprise RAG Ready")

        # ---------------------------------
        # Previous Chat
        # ---------------------------------

        messages = get_messages()

        for msg in messages:

            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        # ---------------------------------
        # Chat Input
        # ---------------------------------

        question = st.chat_input(
            "Ask anything from the uploaded documents..."
        )

        if question:

            add_user_message(question)

            with st.chat_message("user"):
                st.markdown(question)

            with st.spinner("🤖 Thinking..."):

                answer, docs = get_answer(
                    question,
                    retriever,
                    llm
                )

            add_ai_message(answer)

            with st.chat_message("assistant"):

                st.markdown(answer)

                with st.expander("📚 Source Documents"):

                    for i, doc in enumerate(docs):

                        st.markdown(f"### 📄 Source {i+1}")

                        source = doc.metadata.get(
                            "source",
                            "Unknown File"
                        )

                        page = doc.metadata.get(
                            "page",
                            "Unknown"
                        )

                        st.write(f"**File:** {source}")
                        st.write(f"**Page:** {page}")
                        st.write(doc.page_content)
                        st.divider()

        # ---------------------------------
        # Dashboard Metrics
        # ---------------------------------

        st.markdown("---")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("📄 Documents", len(uploaded_files))

        with col2:
            st.metric("📑 Chunks", len(chunks))

        with col3:
            st.metric("🤖 Model", "Gemini")

    except Exception as e:

        st.error("❌ Error Occurred")
        st.exception(e)