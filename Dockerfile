FROM python:3.9.10-alpine3.15

RUN addgroup app && adduser -S -G app app
USER app

# referencing this site for heroku:
# http://sebastien-docs.info/module-not-found-heroku.html
# literally godsend, thank fucking god

ENV HOME /home/app
RUN mkdir -p ${HOME}

WORKDIR ${HOME}

# # http://sebastien-docs.info/module-not-found-heroku.html
# ENV USER app
# ENV HOME /home/${USER}
# RUN mkdir -p ${HOME}
# WORKDIR /home/

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "main.py"]