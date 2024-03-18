#!/usr/bin/env python3
"""Config module"""


class Config(object):
    """A class representing the configuration settings for the application.

    Attributes:
        MAIL_SERVER (str): The SMTP server for sending emails.
        MAIL_PORT (int): The port number for the SMTP server.
        MAIL_USE_TLS (bool): Whether to use TLS for secure connection.
        MAIL_USE_SSL (bool): Whether to use SSL for secure connection.
        MAIL_USERNAME (str): The username for the email account.
        MAIL_PASSWORD (str): The password for the email account.
        MAIL_DEFAULT_SENDER (str): The default sender email address.
    """
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'api.empire0@gmail.com'
    MAIL_PASSWORD = 'juoe smrg pmmm rkbs'
    MAIL_DEFAULT_SENDER = 'api.empire0@gmail.com'
