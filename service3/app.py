from flask import Flask
import random

app = Flask(__name__)

class = ['Barbarian','Bard','Cleric','Druid','Fighter','Monk','Paladin','Ranger','Rogue','Sorcerer','Warlock','Wizard']

@app.route('/get/class')
def get_class():
    return random.choice(class)

if __name__ == '__main__':
    app.run(host='0.0.0.0')