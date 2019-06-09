FROM python:3.7.2-alpine

RUN apk update

COPY . /home/app

WORKDIR /home/app

VOLUME /home/app

EXPOSE 5000
EXPOSE 59153

RUN pip install -r requirements.txt


CMD python main.py run