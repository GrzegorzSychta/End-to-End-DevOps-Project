FROM python:3.12

WORKDIR /app

COPY . /app

EXPOSE 43482

USER root

RUN pip install -r requirements.txt

USER 1001

CMD ["flask", "run", "--host=0.0.0.0", "--port=43482"]


