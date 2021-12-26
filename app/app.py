from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import datetime
import os

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = '{dialect}+{driver}://{user}:{password}@{host}:{port}/{database}?charset={charset_type}'.format(**{
        'dialect': 'mysql',
        'driver': 'pymysql',
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', 'password'),
        'host': os.getenv('DB_HOST', 'host.docker.internal'),
        'port': 5003,
        'database': os.getenv('DB_DATABASE', 'todo_app'),
        'charset_type': 'utf8'})
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

class Task(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(300), nullable=False)
  due = db.Column(db.DateTime, nullable=False)

@app.route("/",methods=['GET','POST'])
def index():
  if request.method == 'GET':
    tasks = Task.query.all()   
    return render_template('index.html', tasks=tasks, tdy=datetime.date.today(), onedy=datetime.timedelta(days=1))

@app.route("/create",methods=['GET','POST'])
def create():
  if request.method == 'POST':
     content = request.form.get('content')
     due     = request.form.get('due')
     task = Task(content=content,due=due)

     db.session.add(task)
     db.session.commit()
     return redirect('/')
  else: 
     return render_template('create.html')

@app.route("/<int:id>/update",methods=['GET','POST'])
def update(id):
  task = Task.query.get(id)
  if request.method == 'GET':
     return render_template('update.html', task=task)
  else: 
     task.content = request.form.get('content')
     task.due = request.form.get('due')
     db.session.commit()
     return redirect('/')

@app.route("/<int:id>/delete",methods=['GET'])
def delete(id):
  task = Task.query.get(id)
  
  db.session.delete(task)
  db.session.commit()
  return redirect('/')

if __name__=="__main__":
  app.run(host="0.0.0.0",port=80,debug=True)
# host: localhost, port:5000
# localhost = 127.0.0.1 IP address