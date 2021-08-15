from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv

app = Flask(__name__)

app.config.update(
    SQLALCHEMY_DATABASE_URI =getenv("DATABASE_URI"),
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    SECRET_KEY=str(os.urandom(16))
)

db = SQLAlchemy(app)

from . import routes
