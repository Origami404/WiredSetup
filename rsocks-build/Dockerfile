FROM python:3.7

ENV TZ Asia/Shanghai

WORKDIR /usr/src/app

RUN pip install --no-cache-dir rsocks

CMD [ "rsocks", "--config=/conf.toml" ]
