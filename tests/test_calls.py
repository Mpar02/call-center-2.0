import pytest
from copy import deepcopy
from seed.data import calls

original_calls = deepcopy(calls)

@pytest.fixture(autouse=True)
def reset_calls():
    calls[:] = deepcopy(original_calls)
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_calls():
    response = client.get("/calls")
    assert response.status_code == 200
    assert isinstance(response.json()["calls"], list)

def test_get_call_by_id():
    response = client.get("/calls/1001")
    assert response.status_code == 200
    assert response.json()["id"] == 1001
    assert "notes" in response.json()

def test_get_call_not_found():
    response = client.get("/calls/9999")
    assert response.status_code == 404

def test_archive_call():
    response = client.patch("/calls/1001/archive")
    assert response.status_code == 200
    assert response.json()["is_archived"] == True

def test_archive_call_not_found():
    response = client.patch("/calls/9999/archive")
    assert response.status_code == 404
    assert response.json()["error"] == "Call not found"
