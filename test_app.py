# test_app.py
import pytest
from flask import url_for


class TestApp:

    def test_ping(self, client):
        res = client.get(url_for('ping'))
        print('inside testapp')
        assert res.status_code == 200
        assert res.json == {'ping': 'pong'}
