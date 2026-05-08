from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_calculation_report_endpoint():
    # Create one calculation first
    response = client.post("/calculations/", json={
        "a": 10,
        "b": 5,
        "type": "Add"
    })

    assert response.status_code == 200

    # Test report endpoint
    response = client.get("/reports/calculations")

    assert response.status_code == 200

    data = response.json()

    assert "total_calculations" in data
    assert "operation_counts" in data
    assert "average_result" in data
    assert "highest_result" in data
    assert "lowest_result" in data
    assert "recent_calculations" in data

    assert data["total_calculations"] >= 1
    assert data["operation_counts"]["Add"] >= 1
