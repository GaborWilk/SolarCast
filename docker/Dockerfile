FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8501
CMD ["streamlit", "run", "streamlit_app/app.py", "--server.port=8501", "--server.enableCORS=false"]
