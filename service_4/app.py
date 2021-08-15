from flask import Flask
import random

app = Flask(__name__)

points = ['one', 'two']

@app.route('/get/points')
def get_points():
    return random.choice(points)
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')