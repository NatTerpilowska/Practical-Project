from flask import Flask
import random

app = Flask(__name__)

pointss = {
    'race': {
        'Dragonborn': 1,
        'Dwarf': 1,
        'Elf' : 1
    },
    'clas': {
        'Barbarian': 2,
        'Dwarf': 2,
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
