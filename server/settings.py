# -*- coding: utf-8 -*-
"""
    file: settings.py
    notes:  Configure Settings for application
"""

import os

class Config(object):
    """ Common config options """
    APPNAME = 'Web Hook Skeleton'
    SUPPORT_EMAIL = 'sergio.bruni@ingv.it'
    VERSION = '1.0.0'
    APPID = 'web_hook_docker'
    SECRET_KEY = os.urandom(24)
    TESTING = False
    LOG_SEVERITY = 'INFO'

class DevelopmentConfig(Config):
    """ Dev environment config options """
    FLASK_ENV='development'
    DEBUG = True
    LOG_SEVERITY = 'DEBUG'
    PROFILE = True

class TestingConfig(Config):
    """ Testing environment config options """
    DEBUG = True
    STAGING = True
    TESTING = True
    LOG_SEVERITY = 'DEBUG'

class ProductionConfig(Config):
    """ Prod environment config options """
    FLASK_ENV = 'production'
    DEBUG = False
    STAGING = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': TestingConfig
}
