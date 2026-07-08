"""
Alert API tests
"""
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_alerts():
    """Test get alerts endpoint"""
    response = client.get("/api/v1/alerts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_alert():
    """Test create alert endpoint"""
    alert_data = {
        "title": "Test Alert",
        "description": "Test Alert Description",
        "severity": "MEDIUM",
        "threat_id": "test-threat-123",
        "source": "detection",
        "data": {"details": "test"}
    }
    response = client.post("/api/v1/alerts", json=alert_data)
    assert response.status_code == 200
    assert response.json()["title"] == alert_data["title"]
