FROM python:3.7.12-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
RUN apt update -y
RUN apt install poppler-utils -y

RUN apt install ffmpeg libsm6 libxext6  -y

# copy project
COPY . /usr/src/app/
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]