import pytest
from flask import url_for


class TestApp:

    def test_hello(self, client):
        res = client.get(url_for('/'))
        assert res.status_code == 200
        assert res.json == {'/': 'Hello World!'}