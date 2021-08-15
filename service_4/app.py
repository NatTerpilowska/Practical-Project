from flask import Flask, request, jsonify
import random

app = Flask(__name__)

pointss = {
    'race': {
        'Dragonborn': 3,
        'Dwarf': 4,
        'Elf' : 7
    },
    'clas': {
        'Barbarian': 4,
        'Bard': 5,
        'Cleric': 2
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
