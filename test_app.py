from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict_valid_input():
    response = client.post("/predict", json={
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    })
    assert response.status_code == 200
    assert "predicted_species" in response.json()

def test_predict_invalid_input():
    response = client.post("/predict", json={})
    assert response.status_code == 422  # Validation error