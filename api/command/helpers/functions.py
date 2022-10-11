from pyparsing import Iterator
import requests
from flask_restful import abort


def extract_pokemons(areas: list) -> Iterator[str]:

    for area in areas:
        for pokemon in area.get("pokemons"):
            yield pokemon.get("pokemon").get("name")


def extract_areas(location: dict) -> Iterator[dict]:

    areas = location.get("areas")

    for area in areas:
        response = requests.get(str(area.get("url")))

        if response.status_code == 200:
            area_info = response.json()
            yield {"name": area_info.get("name"), "pokemons": area_info.get("pokemon_encounters")}
        else:
            abort(400, error=response.json())


def best_location(locations: list) -> dict:

    best_location = {
        "location": '',
        "pokemonTypes": 0
    }

    for location in locations:
        if len(location["pokemons"]) >= best_location["pokemonTypes"]:
            best_location["location"] = location["location"]
            best_location["pokemonTypes"] = len(location["pokemons"])

    return best_location
