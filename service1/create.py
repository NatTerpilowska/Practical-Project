from application import db

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:rooot@35.197.250.227/project2"

db = SQLAlchemy(app)
db.drop_all()
db.create_all()