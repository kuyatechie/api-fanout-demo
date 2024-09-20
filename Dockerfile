FROM python:bookworm

ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/requirements.txt

RUN apt-get update && \
    apt-get install python3-pip -y && \
    pip3 install -r /app/requirements.txt

ADD app /app
WORKDIR /app

ENTRYPOINT [ "python", "manage.py", "runserver" ]
