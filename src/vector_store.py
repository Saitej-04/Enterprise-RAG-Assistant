import os
import shutil
from langchain_community.vectorstores import FAISS

DB_PATH = "vector_db"


def create_vector_store(documents, embedding_model):

    # Delete old vector database
    if os.path.exists(DB_PATH):
        shutil.rmtree(DB_PATH)

    # Create a fresh vector database
    vector_store = FAISS.from_documents(
        documents,
        embedding_model
    )

    # Save the new database
    vector_store.save_local(DB_PATH)

    return vector_store