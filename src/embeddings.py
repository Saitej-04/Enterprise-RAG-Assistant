from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model():

    print("=" * 50)
    print("Loading HuggingFace Embedding Model...")
    print("=" * 50)

    try:

        embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={
                "device": "cpu"
            },
            encode_kwargs={
                "normalize_embeddings": False
            }
        )

        print("=" * 50)
        print("Embedding Model Loaded Successfully!")
        print("=" * 50)

        return embedding_model

    except Exception as e:

        print("=" * 50)
        print("Embedding Model Loading Failed!")
        print(str(e))
        print("=" * 50)

        raise