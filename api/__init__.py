import os
import traceback
from flask import Flask, jsonify
from flask_restful import Api
from api.routes.blueprint import pokemon_location_bp


def create_app(name):

    app = Flask(name)

    Api(app)

    app.register_blueprint(pokemon_location_bp)

    return app
