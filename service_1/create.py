from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

SQLALCHEMY_TRACK_MODIFICATIONS = False
app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=getenv("DATABASE_URI")

db = SQLAlchemy(app)
db.drop_all()
db.create_all()