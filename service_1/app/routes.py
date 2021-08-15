from flask import Flask, request, jsonify, render_template
import requests
from app import app, db
from app.models import Characters


@app.route('/', methods=['GET','POST'])
def home():
    race = requests.get('http://service_2:5000/get/race').text
    clas = requests.get('http://service_3:5000/get/clas').text

    points = requests.post('http://service_4:5000/get/points'.text)

    records = Characters.query.order_by(Characters.id.desc()).limit(15).all()

    outcome = Characters(race=race, clas=clas, points=points)
    db.session.add(outcome)
    db.session.commit()

    return render_template('home.html', outcome=outcome, records=records)
