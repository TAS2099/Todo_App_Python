FROM python:3.8

RUN pip install numpy flask

WORKDIR /app

CMD ["flask", "run", "-h", "0.0.0.0"]