from flask import request, Blueprint
from flask_restful import Api

from api.routes.pokemon_location import PokemonLocation

pokemon_location_bp = Blueprint('pokemon-in-location', __name__,
                                url_prefix="/pokemon-in-location")
api = Api(pokemon_location_bp)

api.add_resource(PokemonLocation, "/", strict_slashes=False)
