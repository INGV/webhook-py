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

@route.route('/api/test', methods=["GET"])
def test():
    return 'test OK!!'

@route.route('/api/get', methods=["GET"])
def get():
    queries.get_webhook(request.args)
    result = (Response('GET-OK', content_type='application/text'), status.HTTP_200_OK)
    return result


@route.route('/api/post', methods=["POST"])
def post():
    body = request.get_json(force=True)
    queries.post_webhook(body)
    result = (Response('POST-OK', content_type='application/text'), status.HTTP_200_OK)
    return result

