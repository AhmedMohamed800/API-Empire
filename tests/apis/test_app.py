#!/usr/bin/env python3
"""Test module for the apis class."""


def test_home(app_clint):
    """Test the home endpoint."""
    response = app_clint.get('/')
    assert response.status_code == 200
