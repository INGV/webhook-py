import json
from server.main import logger
from datetime import date, time, datetime

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

        params = []
        for key, value in args.items():
            params.append(f'{key}={value}')

        msg = 'GET METHOD RECEIVED. PARAMS ARE: ' + '; '.join(params)

        logger.info(msg)
        return True


    def post_webhook(self, body):
        msg = 'POST METHOD RECEIVED. BODY IS: \n' + \
              json.dumps(body, indent=4, sort_keys=True)
        logger.info(msg)
        return True
