import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_courses():
    response = client.get("/courses")
    assert response.status_code == 200

def test_course_details():
    response = client.get("/course-details")
    assert response.status_code == 200

def test_enquiries():
    response = client.get("/enquiries")
    assert response.status_code == 200

def test_internships():
    response = client.get("/internships")
    assert response.status_code == 200

def test_newsletter():
    response = client.get("/newsletter")
    assert response.status_code == 200
