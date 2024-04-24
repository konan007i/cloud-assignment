FROM python:alpine

WORKDIR /app


COPY requirements.txt .

RUN pip install -r requirements.txt


COPY abbas.py .

COPY words.txt .

CMD ["python", "abbas.py"]
