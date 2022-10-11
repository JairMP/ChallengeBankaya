from concurrent.futures import ThreadPoolExecutor

import requests
from flask_restful import abort

from api.command.helpers.constants import KANTO_REGION, LOCATIONS_URL
from api.command.helpers.functions import best_location, extract_areas, extract_pokemons
from api.validators.pokemon_location_validator import BestLocationSchema, LocationSchema, PokemonLocationResponseSchema


def pokemon_location_command(locations: list) -> dict:

    with ThreadPoolExecutor() as executor:

        locations_info = executor.map(get_location_info, locations)

        areas_info = executor.map(get_area_info, locations_info)

    executor.shutdown(wait=True)

    location_response = LocationSchema(
        many=True).dump(areas_info)

    best_location_response = BestLocationSchema().dump(
        best_location(location_response))

    return PokemonLocationResponseSchema().dump({
        "bestLocation": best_location_response,
        "locations": location_response
    })


def get_location_info(location: str) -> dict:

    response = requests.get(LOCATIONS_URL+location)

    if response.status_code == 200:
        location_info = response.json()
        region = location_info.get("region").get("name")

        if region != KANTO_REGION:
            abort(400, error=f"{location} is not located on Kanto region")

        return dict({"name": location_info.get("name"), "areas": location_info.get("areas")})

    abort(400, error="Pokemon API call fail")


def get_area_info(location: dict) -> dict:

    areas_info = list(extract_areas(location))
    pokemons = list(extract_pokemons(areas_info))

    return {"location": location.get("name"), "pokemons": pokemons}
