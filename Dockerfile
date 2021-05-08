FROM python:3.8-slim

RUN mkdir /application
WORKDIR /application

COPY requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED 1

EXPOSE 8080
STOPSIGNAL SIGINT

ENTRYPOINT ["python"]
CMD ["app.py"]