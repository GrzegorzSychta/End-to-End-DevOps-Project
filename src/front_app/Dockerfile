FROM python:3.12

WORKDIR /app

COPY . /app

USER root

RUN pip install -r requirements.txt

EXPOSE 43472

USER 1001

CMD ["flask", "run", "--host=0.0.0.0", "--port=43472"]


