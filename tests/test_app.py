# test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_index(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"ok" in res.data
    assert b"hello world!" in res.data

def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
