# test_app.py
import pytest
from flask import url_for


class TestApp2:

    def test_ping_false_positive2(self, client):
        res = client.get(url_for('ping'))
        assert res.json == {'ping': 'GONG'}, 'THE REQ OF PING DID NOT RETURN gong AS A VALUE'
