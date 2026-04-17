from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_calculation_crud():
    # CREATE
    response = client.post("/calculations/", json={
        "a": 10,
        "b": 5,
        "type": "Add"
    })
    assert response.status_code == 200
    data = response.json()
    calc_id = data["id"]
    assert data["result"] == 15

    # GET ALL
    response = client.get("/calculations/")
    assert response.status_code == 200
    assert len(response.json()) >= 1

    # GET BY ID
    response = client.get(f"/calculations/{calc_id}")
    assert response.status_code == 200
    assert response.json()["id"] == calc_id

    # UPDATE
    response = client.put(f"/calculations/{calc_id}", json={
        "a": 20,
        "b": 4,
        "type": "Divide"
    })
    assert response.status_code == 200
    assert response.json()["result"] == 5

    # DELETE
    response = client.delete(f"/calculations/{calc_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Calculation deleted successfully"

    # VERIFY DELETE
    response = client.get(f"/calculations/{calc_id}")
    assert response.status_code == 404
