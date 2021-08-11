from flask import Flask, request, jsonify

app = Flask(__name__)


strenght = {
    'race': {
        'Dragonborn':2,'Dwarf':0,'Elf':0,'Gnome':0,'Half-Elf':0,'Halfling':0,'Half-Orc':2,'Human':1,'Tiefling':0
    },
    'clas': {
        'Barbarian':0,'Bard':0,'Cleric':0,'Druid':0,'Fighter':0,'Monk':0,'Paladin':0,'Ranger':0,'Rogue':0,'Sorcerer':0,'Warlock':0,'Wizard':0
        
    }
}

dexterity = {
    'race': {
        'Dragonborn':0,'Dwarf':0,'Elf':2,'Gnome':0,'Half-Elf':0,'Halfling':2,'Half-Orc':0,'Human':1,'Tiefling':0
    },
    'clas': {
        'Barbarian':0,'Bard':0,'Cleric':0,'Druid':0,'Fighter':0,'Monk':0,'Paladin':0,'Ranger':0,'Rogue':0,'Sorcerer':0,'Warlock':0,'Wizard':0
        
    }
}

constitution = {
    'race': {
        '': ,
        'Dragonborn':0,'Dwarf':2,'Elf':0,'Gnome':0,'Half-Elf':0,'Halfling':0,'Half-Orc':1,'Human':1,'Tiefling':0
    },
    'clas': {
        'Barbarian':0,'Bard':0,'Cleric':0,'Druid':0,'Fighter':0,'Monk':0,'Paladin':0,'Ranger':0,'Rogue':0,'Sorcerer':0,'Warlock':0,'Wizard':0
    }
}

intelligence = {
    'race': {
        '': ,
        'Dragonborn':0,'Dwarf':0,'Elf':0,'Gnome':2,'Half-Elf':0,'Halfling':0,'Half-Orc':0,'Human':1,'Tiefling':1
    },
    'clas': {
        'Barbarian':0,'Bard':0,'Cleric':0,'Druid':0,'Fighter':0,'Monk':0,'Paladin':0,'Ranger':0,'Rogue':0,'Sorcerer':0,'Warlock':0,'Wizard':0
    }
}

wisdom = {
    'race': {
        'Dragonborn':0,'Dwarf':0,'Elf':0,'Gnome':0,'Half-Elf':0,'Halfling':0,'Half-Orc':0,'Human':1,'Tiefling':0
    },
    'clas': {
        'Barbarian':0,'Bard':0,'Cleric':0,'Druid':0,'Fighter':0,'Monk':0,'Paladin':0,'Ranger':0,'Rogue':0,'Sorcerer':0,'Warlock':0,'Wizard':0  
    }
}
charisma = {
    'race': {
        'Dragonborn':1,'Dwarf':0,'Elf':0,'Gnome':0,'Half-Elf':2,'Halfling':0,'Half-Orc':0,'Human':1,'Tiefling':2
    },
    'clas': {
        'Barbarian':0,'Bard':0,'Cleric':0,'Druid':0,'Fighter':0,'Monk':0,'Paladin':0,'Ranger':0,'Rogue':0,'Sorcerer':0,'Warlock':0,'Wizard':0   
    }
}
@app.route('/post/points', methods=['POST'])
def post_points():
    strenght = request.json['strenght']
    dexterity = request.json['dexterity']
    constitution = request.json['constitution']
    intelligence = request.json['intelligence']
    wisdom = request.json['wisdom']
    charisma = request.json['charisma']

    points = strenght['strenght'][strenght], dexterity['dexterity'][dexterity], constitution['constitution'][constitution], intelligence['intelligence'][intelligence], wisdom['wisdom'][wisdom], charisma['charisma'][charisma]

    return jsonify(points)

if __name__ == '__main__':
    app.run(host='0.0.0.0')