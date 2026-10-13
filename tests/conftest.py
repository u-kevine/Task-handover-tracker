import pytest
from fastapi.testclient import TestClient

from app.main import app, store


@pytest.fixture
def client():
    store.clear()  # every test starts with an empty store
    return TestClient(app)
