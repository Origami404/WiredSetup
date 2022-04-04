FROM python:3.9

ENV TZ Asia/Shanghai

WORKDIR /usr/src/app

RUN pip install --no-cache-dir mitmproxy

COPY ./start.sh .

EXPOSE 8080

CMD [ "bash", "./start.sh" ]
