from flask import Flask, redirect, url_for, request, jsonify, Response
from Game import Game
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app)

# @app.after_request
# def after_request(response):
#   response.headers.add('Access-Control-Allow-Origin', '*')
#   response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#   response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#   return response

@app.route('/battle',methods = ['POST', 'GET'])
def battle():
   if request.method == 'POST':
      fleetOne = request.json['fleetOne']
      fleetTwo = request.json['fleetTwo']

      game = Game(fleetOne, fleetTwo)
      game.battle()

      game_dict = {}
      game_dict['log'] = game.battleLog
      game_dict['destroyment'] = game.shipDestroyment

      return Response(json.dumps(game_dict), mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)
