FROM python:3.8.10-alpine

WORKDIR /app

COPY app .
COPY requirements.txt .
COPY .env .

RUN pip install -r requirements.txt

ENV FLASK_APP="app"
ENV FLASK_ENV="production"

EXPOSE 8000

WORKDIR /

CMD [ "flask", "run" ]
