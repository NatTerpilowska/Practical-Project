from . import db

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    race = db.Column(db.String(100))
    clas = db.Column(db.String(100))
    points = db.Column(db.Float)

db.create_all()

