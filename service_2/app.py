from flask import Flask
import random

app = Flask(__name__)

race = ['Elf','Dragonborn','Hobgoblin']

@app.route('/get/race')
def get_race():
    return random.choice(race)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
 