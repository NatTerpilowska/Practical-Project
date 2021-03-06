from flask import Flask, request, jsonify
import random

app = Flask(__name__)

pointss = {
    'race': {
        'Halfling': 2,
        'Human': 5,
        'Orc' : 1
    },
    'clas': {
        'Paladin': 7,
        'Wizard': 10,
        'Rogue': 10
    }
}
@app.route('/post/points', methods=['POST'])
def post_points():
    race = request.json['race']
    clas = request.json['clas']
    
    points = pointss['race'][race] + pointss['clas'][clas]

    return jsonify(points)
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
