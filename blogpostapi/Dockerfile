from python:3.8.1-buster

COPY config.py .
COPY server.py .
COPY requirements.txt .
COPY blog.db .
EXPOSE 8080
RUN pip install -r requirements.txt
CMD ["python", "server.py"]

