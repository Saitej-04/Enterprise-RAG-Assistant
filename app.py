import streamlit as st

from src.pdf_loader import extract_text_from_pdf
from src.text_splitter import split_text
from src.embeddings import get_embedding_model
from src.vector_store import create_vector_store
from src.retriever import get_retriever
from src.chat_model import get_chat_model


# ---------------------------------
# Page Config
# ---------------------------------

st.set_page_config(
    page_title="Enterprise Financial Intelligence Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Enterprise Financial Intelligence Assistant")

st.markdown("### 📄 Upload Financial Documents")

uploaded_file = st.file_uploader(
    "Choose a PDF",
    type=["pdf"]
)

# ---------------------------------
# Process PDF
# ---------------------------------

if uploaded_file is not None:

    st.success(f"✅ Uploaded Successfully : {uploaded_file.name}")

    st.write("**File Name :**", uploaded_file.name)

    st.write(
        "**File Size :**",
        round(uploaded_file.size / 1024, 2),
        "KB"
    )

    # ---------------------------------
    # Extract Text
    # ---------------------------------

    pdf_text = extract_text_from_pdf(uploaded_file)

    # ---------------------------------
    # Split Text
    # ---------------------------------

    chunks = split_text(pdf_text)

    st.success("✅ PDF Split Successfully")

    st.write("Total Chunks :", len(chunks))

    # ---------------------------------
    # Embedding Model
    # ---------------------------------

    embedding_model = get_embedding_model()

    st.success("✅ Embedding Model Loaded")

    # ---------------------------------
    # FAISS
    # ---------------------------------

    vector_store = create_vector_store(
        chunks,
        embedding_model
    )

    st.success("✅ FAISS Vector Database Created")

    # ---------------------------------
    # Retriever
    # ---------------------------------

    retriever = get_retriever(vector_store)

    st.success("✅ Retriever Created Successfully")

    # ---------------------------------
    # Gemini Model
    # ---------------------------------

    llm = get_chat_model()

    st.success("✅ Gemini Model Loaded")

    # ---------------------------------
    # Ask Question
    # ---------------------------------

    st.markdown("---")

    st.subheader("💬 Ask Questions")

    question = st.text_input(
        "Enter your Question"
    )

    if question:

        docs = retriever.invoke(question)

        context = ""

        for doc in docs:

            context += doc.page_content
            context += "\n\n"

        prompt = f"""
You are an Enterprise Financial Intelligence Assistant.

Answer only from the given context.

If the answer is not available in the context, reply:

"I could not find the answer in the uploaded document."

Context:

{context}

Question:

{question}
"""

        response = llm.invoke(prompt)

        st.subheader("🤖 AI Response")

        st.write(response.content)

        st.markdown("---")

        st.subheader("📚 Source Chunks")

        for i, doc in enumerate(docs):

            st.markdown(f"### Source {i+1}")

            st.write(doc.page_content)

            st.divider()