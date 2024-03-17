#!/usr/bin/env python3
""" config module for flask app """


class Config(object):
    """ config class """
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'api.empire0@gmail.com'
    MAIL_PASSWORD = 'juoe smrg pmmm rkbs'
    MAIL_DEFAULT_SENDER = 'api.empire0@gmail.com'
