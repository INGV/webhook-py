from flask import Blueprint, jsonify, render_template

from flask import (
    request,
    Response
)
from  flask_api import status

from server.main.api.queries import Queries
route = Blueprint('webserver', __name__)

from flask_cors import CORS
cors = CORS(route, resources={r"/*": {"origins": "*"}})

queries = Queries()

# @route.route('/api/test', methods=["GET"])
# def test():
#     return 'test OK!!'

@route.route('/api/whook', methods=["GET"])
def get():
    result_struct, status = queries.get_webhook(request.args)
    result = (Response(result_struct, content_type='application/json'), status)
    return result


@route.route('/api/whook', methods=["POST"])
def post():
    body = None
    if request.data:
        body = request.get_json(force=True)
    result_struct, status = queries.post_webhook(request.args, body)
    result = (Response(result_struct, content_type='application/json'), status)
    return result
