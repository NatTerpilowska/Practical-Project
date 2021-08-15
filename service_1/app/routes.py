from app import app, db
from app.models import Characters
from flask import Flask, json, request, jsonify, render_template
import requests


@app.route('/')
def home():
    race = requests.get('http://service_2:5000/get/race').text
    clas = requests.get('http://service_3:5000/get/clas').text
    
    payload = {'race': race, 'clas': clas}
    points = requests.post('http://service_4:5000/post/points', json=payload).json()

    records = Characters.query.order_by(Characters.id.desc()).limit(15).all()

    outcome = Characters(race=race, clas=clas, points=points)
    db.session.add(outcome)
    db.session.commit()
    history = Characters.query.all()

    return render_template('home.html', outcome=outcome, race=race, clas=clas, points=points, records=records, history=history)

