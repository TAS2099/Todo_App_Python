FROM python:3.8.12

RUN pip install flask flask-sqlalchemy  PyMySQL flask-bootstrap

WORKDIR /app

CMD ["python", "/app/app/app.py"]