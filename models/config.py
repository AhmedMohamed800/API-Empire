#!/usr/bin/env python3
"""Config module"""
import re


def validate_email(email):
    """validate email"""
    pattern = r'^\S+@\S+\.\S+$'
    if not re.match(pattern, email):
        x = 'Email should follow this pattern example@example.exmaple'
        raise ValueError(x)



def check_password(password):
    """check password"""
    if len(password) < 7:
        raise ValueError('Password too short')
    if not re.search("[a-z]", password):
        raise ValueError('Password must contain a lowercase letter')
    if not re.search("[A-Z]", password):
        raise ValueError('Password must contain an uppercase letter')
    if not re.search("[0-9]", password):
        raise ValueError('Password must contain a number')
    if not re.search("[_@$]", password):
        raise ValueError('Password must contain a special character')


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
