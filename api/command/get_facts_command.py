import requests
from flask_restful import abort
from concurrent.futures import ThreadPoolExecutor

from api.command.constants import URL


def get_facts_command(facts_number: int) -> dict:

    with ThreadPoolExecutor() as executor:
        results = executor.map(api_call, [1]*facts_number)

        for result in results:
            print(result)

    executor.shutdown(wait=True)

    return {}


def api_call(id: int) -> dict:

    response = requests.get(URL)

    if response.status_code == 200:
        return response.json()

    return {"error": "API call fail"}
