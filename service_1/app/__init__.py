from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from os import getenv

app = Flask(__name__)

app.config.update(
    SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URI")
)


db = SQLAlchemy(app)

from . import routes
