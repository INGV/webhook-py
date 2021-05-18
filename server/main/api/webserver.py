import flask_api.status
from flask import Blueprint, jsonify, render_template

from flask import (
    request,
    Response,
    make_response
)
from  flask_api import status

from server.main.api.queries import Queries
route = Blueprint('webserver', __name__)

from flask_cors import CORS
cors = CORS(route, resources={r"/*": {"origins": "*"}})
from pathlib import Path
import logging
import logging.handlers
import sys

from server.settings import config
import os

@route.route('/api/test', methods=["GET"])
def test():
    return 'test OK!!'

@route.route('/api/get', methods=["GET"])
def get():
    retval = queries.get_webhook(request.args)
    result = (Response('GET-OK', content_type='application/text'), status.HTTP_200_OK)
    return result


@route.route('/api/post', methods=["POST"])
def post():
    body = request.get_json(force=True)
    retval = queries.post_webhook(body)
    result = (Response('POST-OK', content_type='application/text'), status.HTTP_200_OK)
    return result


def create_logger():
    log_name = Path(__file__).stem
    logger = logging.getLogger(log_name)

    formatter = logging.Formatter(fmt='[%(asctime)s.%(msecs)03d] - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    numeric_level = getattr(logging, app_settings.LOG_SEVERITY, None)
    logger.setLevel(numeric_level)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(numeric_level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    if not os.path.isdir(app_settings.LOG_FOLDER):
        os.makedirs(app_settings.LOG_FOLDER, 493)

    log_file_name = os.path.join(app_settings.LOG_FOLDER, 'whook.log')
    f_handler = logging.handlers.RotatingFileHandler(log_file_name, maxBytes=1000000, backupCount=10)
    f_handler.setLevel(numeric_level)
    f_handler.setFormatter(formatter)
    logger.addHandler(f_handler)

    return logger

config_type = os.getenv('FLASK_CONFIG') or 'default'
app_settings = config[config_type]
logger = create_logger()
logger.info("Server Started")
queries = Queries(logger)

if __name__ == '__main__': # this part runs only development
    from server.main.api import create_app_blueprint
    application = create_app_blueprint(config_type)
    application.run(debug=True, use_debugger=False, use_reloader=False, port=4300, host='0.0.0.0')


