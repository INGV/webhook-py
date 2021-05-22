# this script runs the Flask Development Server
# Not used in production !!!
from server.main.api import create_app_blueprint
#if __name__ == '__main__':
application = create_app_blueprint('development')
application.run(debug=True, use_debugger=False, use_reloader=False, port=4300, host='0.0.0.0')
