from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    race = requests.get('http://service-2:5000/get/race').text
    class = requests.get('http://service-3:5000/get/class').text

    payload = {'race': race, 'class': class}
    points = requests.post('http://service-4:5000/post/points', json=payload).json()

    return f"You rolled a {race} and a {class} and got {points}.\n"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')