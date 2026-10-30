import pytest
from githubaction import app
from flask import Flask

@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

def test_request_example(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data
    
    





