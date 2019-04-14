FROM ubuntu:latest
LABEL mmmsr "mmmsr"

# 以降のインストールでタイムゾーン設定で止まるのを防ぐため、先にタイムゾーンを設定する
RUN apt-get update -y && apt-get install -y tzdata
ENV TZ=Asia/Tokyo

RUN apt-get update -y && apt-get install -y python3 python3-pip build-essential git curl postgresql postgresql-client postgresql-contrib libpq-dev

RUN curl https://cli-assets.heroku.com/install.sh | sh
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
