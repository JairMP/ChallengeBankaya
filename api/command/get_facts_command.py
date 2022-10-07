import requests
from flask_restful import abort


def get_facts_command(facts_number: int) -> dict:

    try:
        facts = requests.get(
            'https://cat-fact.herokuapp.com/facts', timeout=10)
    except:
        abort(400, error="Cats Facts API Error")

    if facts.status_code != 200:
        abort(400, error="Cats Facts API Error")

    return facts
