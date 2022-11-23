FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY ./ /app
ENV FLASK_APP=main.py
ENV FLASK_DEBUG=1
EXPOSE 5000
