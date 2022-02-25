FROM python:3.9.10-alpine3.15

RUN addgroup app && adduser -S -G app app
USER app

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "-u", "main.py"]