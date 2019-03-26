FROM ubuntu:latest
LABEL mmmsr "mmmsr"
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip build-essential git curl
RUN curl https://cli-assets.heroku.com/install.sh | sh
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
