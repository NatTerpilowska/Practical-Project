from flask import Flask
import random

app = Flask(__name__)

clas = ['Barbarian','Bard','Cleric','Druid','Fighter','Monk','Paladin','Ranger','Rogue','Sorcerer','Warlock','Wizard']

@app.route('/get/clas')
def get_clas():
    return (random.choice(clas))
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')