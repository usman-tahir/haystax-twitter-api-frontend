FROM python:3.6-slim

RUN apt-get update -y && apt-get install -y python-dev build-essential vim less

COPY . /opt/haystax-twitter-api-frontend
WORKDIR /opt/haystax-twitter-api-frontend

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]