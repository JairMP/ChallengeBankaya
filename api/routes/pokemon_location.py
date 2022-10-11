from flask import request
from flask_restful import Resource, abort
from marshmallow import ValidationError

from api.command.pokemon_location_command import pokemon_location_command
from api.validators.pokemon_location_validator import PokemonLocationPayloadSchema


class PokemonLocation(Resource):
    def post(self) -> dict:

        try:
            locations = PokemonLocationPayloadSchema().load(request.get_json())
        except ValidationError as err:
            abort(400, errors=err.messages)

        return pokemon_location_command(locations.get("locations"))
