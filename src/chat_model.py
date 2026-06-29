import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def get_chat_model():

    llm = ChatGoogleGenerativeAI(
        model=os.getenv("MODEL_NAME"),
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0
    )

    return llm