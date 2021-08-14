from flask import Flask, request, jsonify

app = Flask(__name__)

points = {
    'race': {
        'Dragonborn':2,'Dwarf':0,'Elf':0,'Gnome':0,'Half-Elf':0,'Halfling':0,'Half-Orc':2,'Human':1,'Tiefling':0
    },
    'clas': {
        'Barbarian':0,'Bard':0,'Cleric':0,'Druid':0,'Fighter':0,'Monk':0,'Paladin':0,'Ranger':0,'Rogue':0,'Sorcerer':0,'Warlock':0,'Wizard':0
        
    }
}

@app.route('/post/points', methods=['POST'])
def post_points():
    strenght = request.json['strenght']
   

    points = strenght
    return jsonify(points)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')