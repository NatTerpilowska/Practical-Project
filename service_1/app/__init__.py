import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from os import getenv

app = Flask(__name__)

app.config.update(
    SQLALCHEMY_DATABASE_URI =getenv("DATABASE_URI"),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SECRET_KEY=str(os.urandom(16))
)


db = SQLAlchemy(app)

from . import routes
