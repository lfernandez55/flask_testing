# test_app.py
import pytest
from flask import url_for


class TestApp:

    def test_ping(self, client):
        res = client.get(url_for('ping'))
        assert res.status_code == 200
        assert res.json == {'ping': 'pong'}

    def test_ping_false_positive(self, client):
        res = client.get(url_for('ping'))
        assert res.status_code == 400, 'Request ping did not result in a 400 error'
