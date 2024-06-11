FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN python -m nltk.downloader -d /usr/local/share/nltk_data -r nltk.txt

CMD ["python", "app.py"]
