from flask import Flask
import random

app = Flask(__name__)

clas = ['Bard', 'Sorcerer', 'Cleric']
@app.route('/get/clas')
def get_clas():
    return random.choice(clas)
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')