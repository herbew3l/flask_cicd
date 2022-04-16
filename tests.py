# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask_cicd.apps.tests.conftest import app

with app.test_client() as test_client:
        res = test_client.get('/login')
        assert res.status_code == 308