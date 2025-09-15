import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Sample data for POST requests
course_data = {
    "title": "Test Course",
    "description": "A test course.",
    "duration": "10h",
    "image": "test.jpg",
    "level": "Beginner",
    "rating": 5,
    "lessons": "5",
    "path": "test-course"
}
course_details_data = {
    "path": "test-course-details",
    "data": {"info": "details"}
}
enquiry_data = {
    "firstName": "John",
    "lastName": "Doe",
    "email": "john@example.com",
    "phone": "1234567890",
    "message": "Test enquiry"
}
internship_data = {
    "email": "intern@example.com"
}
newsletter_data = {
    "email": "newsletter@example.com"
}

def test_create_course():
    response = client.post("/courses/", json=course_data)
    assert response.status_code in [200, 201]
    assert "id" in response.json()

def test_create_course_details():
    response = client.post("/course-details", json=course_details_data)
    assert response.status_code in [200, 201]
    assert "id" in response.json()

def test_create_enquiry():
    response = client.post("/enquiries/", json=enquiry_data)
    assert response.status_code in [200, 201]
    assert "id" in response.json()

def test_create_newsletter():
    response = client.post("/newsletter/", json=newsletter_data)
    assert response.status_code in [200, 201]
    assert "id" in response.json()
