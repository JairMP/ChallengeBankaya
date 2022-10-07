from flask import request
from flask_restful import Resource

from api.command.get_facts_command import get_facts_command


class Get_Facts(Resource):
    def get(self, facts_number: int) -> dict:
        facts = get_facts_command(facts_number)
        return {"recipe": facts}
