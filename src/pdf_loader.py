from pypdf import PdfReader
from langchain.schema import Document


def extract_text_from_pdfs(uploaded_files):

    documents = []

    for uploaded_file in uploaded_files:

        pdf_reader = PdfReader(uploaded_file)

        file_name = uploaded_file.name

        for page_number, page in enumerate(pdf_reader.pages, start=1):

            page_text = page.extract_text()

            if page_text:

                documents.append(
                    Document(
                        page_content=page_text,
                        metadata={
                            "source": file_name,
                            "page": page_number
                        }
                    )
                )

    return documents