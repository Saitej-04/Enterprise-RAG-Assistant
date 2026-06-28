FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install torch==2.5.1+cpu \
    --index-url https://download.pytorch.org/whl/cpu

RUN pip install --default-timeout=1000 -r requirements.txt
COPY . .

EXPOSE 8501

CMD ["streamlit","run","app.py","--server.address=0.0.0.0","--server.port=8501"]