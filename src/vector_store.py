import os
from langchain_community.vectorstores import FAISS

DB_PATH = "vector_db"


def create_vector_store(documents, embedding_model):

    # If vector database already exists, load it
    if os.path.exists(DB_PATH):

        vector_store = FAISS.load_local(
            DB_PATH,
            embedding_model,
            allow_dangerous_deserialization=True
        )

        return vector_store

    # Otherwise create a new vector database
    vector_store = FAISS.from_documents(
        documents,
        embedding_model
    )

    # Save the database
    vector_store.save_local(DB_PATH)

    return vector_store