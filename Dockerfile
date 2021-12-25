FROM python:3.8

RUN pip install flask flask-sqlalchemy  PyMySQL

WORKDIR /app

CMD ["python", "/app/app/app.py"]