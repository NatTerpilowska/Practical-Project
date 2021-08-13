from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    race = requests.get('http://service_2:5000/get/race').text
    clas = requests.get('http://service_3:5000/get/class').text

    payload = {'race': race, 'clas': clas}
    points = requests.post('http://service_4:5000/post/points', json=payload).json()

    return f"You rolled a {race} and a {clas} and got {points}.\n"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')