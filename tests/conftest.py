#!/usr/bin/env python3
"""pytest configuration file."""
import pytest


@pytest.fixture()
def app_clint():
    """Create a new instance of the Flask test client."""
    from api.v1.app import app
    return app.test_client()
