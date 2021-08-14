from flask import Flask
import random

app = Flask(__name__)

race = ['Dragonborn','Dwarf','Elf','Gnome','Half-Elf','Halfling','Half-Orc','Human','Tiefling']

@app.route('/get/race')
def get_race():
    return jsonify(random.choice(race))

if __name__ == '__main__':
    app.run(host='0.0.0.0')