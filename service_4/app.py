from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/post/points', methods=['POST'])
def points():
     points = {
        "Dragonborn" : {
            "Barbarian" : "aa", 
            "Bard" : "aa"
            "Cleric" : "aa", 
            "Druid": "aaa"
        },

 info = request.json 
return Response(points[info["character_race"]][info["character_clas"]], mimetype='text/plain')