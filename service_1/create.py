from flask import Flask
from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@34.142.41.159/project2"

db = SQLAlchemy(app)
db.drop_all()
db.create_all()