"""
Threat API tests
"""
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_root():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "XDR Backend API" in response.json()["message"]


def test_get_threats():
    """Test get threats endpoint"""
    response = client.get("/api/v1/threats")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_threat():
    """Test create threat endpoint"""
    threat_data = {
        "title": "Test Threat",
        "description": "Test Description",
        "severity": "HIGH",
        "threat_type": "malware",
        "source": "endpoint",
        "indicators": {"hash": "abc123"}
    }
    response = client.post("/api/v1/threats", json=threat_data)
    assert response.status_code == 200
    assert response.json()["title"] == threat_data["title"]
