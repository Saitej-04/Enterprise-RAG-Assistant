# 📊 Enterprise Financial Intelligence Assistant

An Enterprise-grade Retrieval-Augmented Generation (RAG) application built using **Streamlit**, **LangChain**, **Google Gemini**, **FAISS**, and **Hugging Face Embeddings**.

The application allows users to upload multiple PDF documents, perform semantic search, and ask natural language questions to receive context-aware AI-generated responses with source citations.

---

# 🚀 Features

- 📄 Multiple PDF Upload
- 🔍 Semantic Search using FAISS
- 🤖 Google Gemini 2.5 Flash Integration
- 🧠 Hugging Face Sentence Embeddings
- 💬 ChatGPT-style Chat Interface
- 📝 Conversation Memory
- 📚 Source Citations
- 📑 Automatic PDF Chunking
- ⚡ Fast Document Retrieval
- 🎯 Context-aware AI Responses

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend |
| Streamlit | User Interface |
| LangChain | RAG Pipeline |
| Google Gemini | Large Language Model |
| HuggingFace | Embedding Model |
| FAISS | Vector Database |
| PyPDF | PDF Processing |

---

# 📂 Project Structure

```text
Enterprise-RAG-Assistant
│
├── app.py
├── requirements.txt
├── README.md
│
├── src
│   ├── chat_model.py
│   ├── embeddings.py
│   ├── memory.py
│   ├── pdf_loader.py
│   ├── prompt_template.py
│   ├── rag_chain.py
│   ├── retriever.py
│   ├── text_splitter.py
│   └── vector_store.py
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Saitej-04/Enterprise-RAG-Assistant.git
```

Go to the project folder

```bash
cd Enterprise-RAG-Assistant
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run the Application

```bash
streamlit run app.py
```

---

# 📸 Workflow

```
Upload PDFs
      ↓
Extract Text
      ↓
Split into Chunks
      ↓
Generate Embeddings
      ↓
Store in FAISS
      ↓
Semantic Retrieval
      ↓
Google Gemini
      ↓
AI Response with Citations
```

---

# 🎯 Current Features

✅ Multiple PDF Upload

✅ FAISS Vector Database

✅ Google Gemini Integration

✅ Hugging Face Embeddings

✅ ChatGPT-style UI

✅ Conversation Memory

✅ Source Citations

---

# 🚀 Future Enhancements

- Persistent FAISS Storage
- Docker Support
- Kubernetes Deployment
- Jenkins CI/CD Pipeline
- AWS EKS Deployment
- User Authentication

---

# 👨‍💻 Author

**Sai Teja Korla**

GitHub: https://github.com/Saitej-04

LinkedIn: https://linkedin.com/in/sai-teja-korla-b40822318

---

⭐ If you like this project, give it a star!