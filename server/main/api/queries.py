import json
from server.main import logger
from datetime import date, time, datetime
from flask_api import status as http_status_code

class Queries(object):
    @staticmethod
    def dateConverter(o):
        if isinstance(o, (date, datetime)):
            return o.__str__()
        elif isinstance(o, (date, time)):
            return o.__str__()

    def __init__(self):
        pass

    def get_webhook(self, args):
        return_struct = {
          "status": http_status_code.HTTP_200_OK,
          "title": "OK",
          "detail": "The service is working properly"
        }

        params = []
        for key, value in args.items():
            params.append(f'{key}={value}')

        msg = 'GET METHOD RECEIVED. PARAMS ARE: ' + '; '.join(params)

        logger.info(msg)
        return json.dumps(return_struct), http_status_code.HTTP_200_OK


    def post_webhook(self, args, form, body):
        return_struct = {
          "status": http_status_code.HTTP_200_OK,
          "title": "OK",
          "detail": "The service is working properly"
        }

        msg = 'POST METHOD RECEIVED'
        logger.info(msg)
        if body:
            msg = 'JSON: \n' + \
                  json.dumps(body, indent=4, sort_keys=True)
            logger.info(msg)

        if args:
            params = []
            for key, value in args.items():
                params.append(f'{key}={value}')

            msg = 'QUERY STRING: ' + '; '.join(params)
            logger.info(msg)

        if form:
            params = []
            for key, value in form.items():
                params.append(f'{key}={value}')

            msg = 'FORMS: ' + '; '.join(params)
            logger.info(msg)

        return json.dumps(return_struct), http_status_code.HTTP_200_OK