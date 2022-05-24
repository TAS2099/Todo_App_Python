FROM python:3.8.13

RUN pip install flask flask-sqlalchemy  PyMySQL flask-bootstrap gunicorn

WORKDIR /app

CMD ["python", "/app/app/app.py"]