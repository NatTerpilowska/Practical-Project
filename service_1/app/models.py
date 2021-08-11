from . import db

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    race = db.Column(db.String(100))
    class = db.Column(db.String(100))
    points = db.Column(db.Integer))