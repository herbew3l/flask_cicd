# -*- coding: utf-8 -*-
from __future__ import absolute_import

import pytest
from run import app as flask_app

@pytest.fixture(scope='session')
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_login_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/login' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/login')
        assert res.status_code == 308
        
        
