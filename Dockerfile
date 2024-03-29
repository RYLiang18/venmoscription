FROM python:3.9.10-alpine3.15

RUN addgroup app && adduser -S -G app app
USER app

# referencing this site for heroku:
# http://sebastien-docs.info/module-not-found-heroku.html

ENV HOME /home/app
RUN mkdir -p ${HOME}

WORKDIR ${HOME}

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "/home/app/main.py"]