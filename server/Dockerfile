FROM python:3.6-slim

RUN python -m pip install rasa==1.8
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /server
WORKDIR /server
COPY . /server

CMD rasa run actions
