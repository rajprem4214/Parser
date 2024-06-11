FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN python download_nltk_data.py

CMD ["python", "app.py"]
