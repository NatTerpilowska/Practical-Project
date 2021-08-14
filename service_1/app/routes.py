from flask import Flask, request, jsonify, render_template
import requests
from app import app, db
from app.models import Characters


@app.route('/', methods=['GET','POST'])
def home():
    race = requests.get('http://service_2:5000/get/race').text
    clas = requests.get('http://service_3:5000/get/class').text

    data = [race, clas]
    points = requests.post('http://service_4:5000/post/points', data)

    records = Character.query.order_by(Character.id.desc()).limit(15).all()

    outcome = Character(race=race, clas=clas, points=points)
    db.session.add(outcome)
    db.session.commit()

    return render_template('home.html', points=points, records=records)
