from flask import request, Blueprint
from flask_restful import Api

from api.routes.get_facts import Get_Facts

cat_facts_bp = Blueprint('cat_facts', __name__, url_prefix="/cat_facts")
api = Api(cat_facts_bp)

api.add_resource(Get_Facts, '/<int:facts_number>')
