# 🚀 Enterprise Financial Intelligence Assistant (RAG)

An AI-powered Enterprise Financial Intelligence Assistant built using **Retrieval-Augmented Generation (RAG)**. The application allows users to upload enterprise PDF documents, ask questions in natural language, and receive accurate AI-generated answers with source citations.

---

## 📌 Project Overview

This project was developed as part of the Enterprise GenAI Capstone Project.

The application processes enterprise documents, converts them into vector embeddings, stores them in a FAISS vector database, retrieves relevant information, and generates grounded responses using Google's Gemini LLM.

---

## ✨ Features

* 📄 Upload one or more PDF documents
* 📚 Automatic PDF parsing
* ✂️ Intelligent text chunking
* 🤖 HuggingFace Embeddings
* 🔍 FAISS Vector Database
* 💬 Natural Language Question Answering
* 🧠 Google Gemini Integration
* 📖 Source Document Citations
* 💾 Chat History
* 🌐 Streamlit Web Interface
* 🐳 Docker Containerization
* ⚙️ Jenkins CI/CD Pipeline
* ☸️ Kubernetes Deployment

---

# 🏗 Architecture

```
                User
                  │
                  ▼
          Streamlit Web App
                  │
                  ▼
            Upload PDF Files
                  │
                  ▼
             PDF Extraction
                  │
                  ▼
            Text Chunking
                  │
                  ▼
      HuggingFace Embeddings
                  │
                  ▼
        FAISS Vector Database
                  │
                  ▼
             Retriever
                  │
                  ▼
         Google Gemini LLM
                  │
                  ▼
        AI Generated Response
                  │
                  ▼
        Source Document Citation
```

---

# ⚙️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI / LLM

* Google Gemini 2.5 Flash

### Embeddings

* HuggingFace Sentence Transformers

### Vector Database

* FAISS

### Framework

* LangChain

### DevOps

* Docker
* Docker Hub
* Jenkins
* Kubernetes

---

# 📂 Project Structure

```
Enterprise-RAG-Assistant/
│
├── app.py
├── Dockerfile
├── Jenkinsfile
├── deployment.yaml
├── service.yaml
├── configmap.yaml
├── secret.yaml
├── requirements.txt
│
├── src/
│   ├── pdf_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── chat_model.py
│   ├── rag_chain.py
│   ├── memory.py
│   └── prompt_template.py
│
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Saitej-04/Enterprise-RAG-Assistant.git
```

Go to project directory

```bash
cd Enterprise-RAG-Assistant
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

# 🐳 Docker

Build Image

```bash
docker build -t enterprise-rag .
```

Run Container

```bash
docker run -p 8501:8501 enterprise-rag
```

---

# ☸ Kubernetes

Deploy application

```bash
kubectl apply -f configmap.yaml
kubectl apply -f secret.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

Check Pods

```bash
kubectl get pods
```

Check Services

```bash
kubectl get svc
```

---

# 🔄 CI/CD Pipeline

GitHub

⬇

Jenkins Pipeline

⬇

Docker Build

⬇

Docker Hub Push

⬇

Kubernetes Deployment

⬇

Streamlit Application

---

# 📸 Application Workflow

1. Upload PDF Documents
2. Extract Text
3. Split into Chunks
4. Generate Embeddings
5. Store in FAISS
6. Retrieve Relevant Chunks
7. Generate Response using Gemini
8. Display Source Citations

---

# 📈 Future Enhancements

* Persistent Vector Database
* Authentication
* Multi-user Support
* Database Integration
* Cloud Deployment
* Chat Export
* Role-based Access

---

# 👨‍💻 Author

**Sai Teja Korla**

GitHub:
https://github.com/Saitej-04

LinkedIn:
https://linkedin.com/in/sai-teja-korla-b40822318

---
