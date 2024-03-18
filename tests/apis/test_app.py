#!/usr/bin/env python3
"""Test module for the apis class."""
from tests.conftest import app_clint


def test_home(app_clint):
    """Test the home endpoint."""
    response = app_clint.get('/')
    assert response.status_code == 404

def test_email(app_clint):
    """Test the email endpoint."""
    data = {}
    data['email'] = 'anything@gmail.com'
    data['first_name'] = 'anything'
    data['password'] = 'anything'
    data['last_name'] = 'anything'
    response = app_clint.post('/signup', json=data)
    assert response.status_code == 200
