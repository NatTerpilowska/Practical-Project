from flask import Flask
import requests
from . import app, db
from .models import Character

app = Flask(__name__)

@app.route('/')
def index():
    race = requests.get('http://service-2:5000/get/race').text
    class = requests.get('http://service-3:5000/get/class').text

    payload = {'race': race, 'class': class}
    points = requests.post('http://service-4:5000/post/points', json=payload).json()
    
    records = Character.query.order_by(Character.id.desc()).limit(5).all()

    
    characters = Character(race=race, class=class, points=points)
    db.session.add(points)
    db.session.commit()

    return render_template("index.html", points=points, records=records)
