"""
Incident API tests
"""
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_incidents():
    """Test get incidents endpoint"""
    response = client.get("/api/v1/incidents")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_incident():
    """Test create incident endpoint"""
    incident_data = {
        "title": "Test Incident",
        "description": "Test Incident Description",
        "severity": "CRITICAL",
        "affected_assets": ["server1", "server2"]
    }
    response = client.post("/api/v1/incidents", json=incident_data)
    assert response.status_code == 200
    assert response.json()["title"] == incident_data["title"]
