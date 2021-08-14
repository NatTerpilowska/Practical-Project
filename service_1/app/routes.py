from flask import Flask, request, jsonify, render_template
import requests
from app import app, db
from app.models import Characters
 

@app.route("/")
def home():
    return render_template('home.html')


#@app.route('/get')
#def home():
   # race = requests.get('http://service_2:5000/get/race').text
  #  clas = requests.get('http://service_3:5000/get/class').text
#
  #  payload = {'race': race, 'clas': clas}
  #  points = requests.post('http://service_4:5000/post/points', json=payload).json()
    
  #  records = Character.query.order_by(Character.id.desc()).limit(5).all()

    
   # characters = Character(race=race, clas=clas, points=points)
   # db.session.add(points)
    #db.session.commit()

    #return render_template("home.html", points=points, records=records)
