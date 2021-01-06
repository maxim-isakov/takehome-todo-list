from fastapi.testclient import TestClient

from todolist import app

client = TestClient(app)

def test_add_to_list():
    response = client.post("/list/", json={"itemName": "Get Dressed", "priority": 1})
    assert response.status_code == 201
    assert response.json() == {
        "1": "Get Dressed",
    }


def test_add_multiple_to_list():
    client.post("/list/", json={"itemName": "Get Dressed", "priority": 1})
    response = client.post("/list/", json={"itemName": "Brush Teeth", "priority": 2})
    assert response.status_code == 201
    assert response.json() == {
        "1": "Get Dressed",
        "2": "Brush Teeth"
    }

def test_remove_from_list():
    client.post("/list/", json={"itemName": "Get Dressed", "priority": 1})
    client.post("/list/", json={"itemName": "Brush Teeth", "priority": 2})
    response = client.delete("/list/1")
    assert response.status_code == 200
    assert response.json() == {
        "2": "Brush Teeth"
    }

def test_get_list():
    client.post("/list/", json={"itemName": "Get Dressed", "priority": 1})
    client.post("/list/", json={"itemName": "Brush Teeth", "priority": 2})
    client.post("/list/", json={"itemName": "Read Book", "priority": 5})
    response = client.get("/list/")
    assert response.status_code == 200
    assert response.json() == {
        "1": "Get Dressed",
        "2": "Brush Teeth",
        "5": "Read Book",
    }

def test_get_missing_list():
    client.post("/list/", json={"itemName": "Get Dressed", "priority": 1})
    client.post("/list/", json={"itemName": "Brush Teeth", "priority": 2})
    client.post("/list/", json={"itemName": "Read Book", "priority": 5})
    response = client.get("/missing-list/")
    assert response.status_code == 200
    assert response.json() == [3, 4]