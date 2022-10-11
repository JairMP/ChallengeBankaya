import pytest

from api import create_app


app = create_app(__name__)


def test_pokemon_location_no_locations():
    response = app.test_client().post(
        "/pokemon-in-location", json={"locations": []})

    assert response.status_code == 400
    assert response.json["errors"] == {
        "locations": [
            "Shorter than minimum length 1."
        ]
    }


def test_pokemon_location_bad_location():
    response = app.test_client().post(
        "/pokemon-in-location", json={"locations": ["canalave-city"]})

    assert response.status_code == 400
    assert response.json["error"] == "canalave-city is not located on Kanto region"


def test_pokemon_location_success():
    response = app.test_client().post(
        "/pokemon-in-location", json={"locations": ["pallet-town"]})

    assert response.status_code == 200
    assert response.json["locations"]
    assert response.json["bestLocation"]
