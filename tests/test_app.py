import os
import sys

# Ensure `hello_flask` package is importable when running tests from workspace root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest

from app.app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_root(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"<html" in resp.data.lower()
    assert b"bmw" in resp.data.lower()
