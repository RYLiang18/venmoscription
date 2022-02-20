FROM python:3.9.10-alpine3.15

RUN addgroup app && adduser -S -G app app
USER app

WORKDIR /app

# this is so that we have access to venmoscription.logs volume
RUN mkdir logs 

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["python", "main.py"]
