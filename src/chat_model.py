import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def get_chat_model():

    llm = ChatGoogleGenerativeAI(
        model=os.getenv("MODEL_NAME", "gemini-3.1-flash-lite"),
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0
    )

    return llm