from src.prompt_template import get_prompt


def get_answer(question, retriever, llm):

    docs = retriever.invoke(question)

    context = ""

    for doc in docs:
        context += doc.page_content
        context += "\n\n"

    prompt = get_prompt(context, question)

    response = llm.invoke(prompt)

    return response.content, docs