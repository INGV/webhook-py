from contextlib import closing
import json

from datetime import date, time, datetime, timedelta
from server.settings import config

class Queries(object):
    @staticmethod
    def dateConverter(o):
        if isinstance(o, (date, datetime)):
            return o.__str__()
        elif isinstance(o, (date, time)):
            return o.__str__()

    def __init__(self, logger):
        self.logger = logger

    def get_webhook(self, args):
        msg = 'GET METHOD RECEIVED. PARAMS ARE: '

        params = []
        for key, value in args.items():
            params.append(f'{key}={value}')

        msg = 'GET METHOD RECEIVED. PARAMS ARE: ' + '; '.join(params)

        self.logger.info(msg)
        return True


    def post_webhook(self, body):
        msg = 'POST METHOD RECEIVED. BODY IS: \n' + \
              json.dumps(body, indent=4, sort_keys=True)
        self.logger.info(msg)
        return True
