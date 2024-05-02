# Test cases for the user endpoint
import asyncio

import pytest
from fastapi.testclient import TestClient


def test_create_user_success(client: TestClient):
    # Define a payload that represents a valid user creation request
    response = client.post("/users/", json={"username": "newuser", "email": "newuser@example.com"})
    assert response.status_code == 200
    assert response.json() == {"username": "newuser", "id": 1, "email": "newuser@example.com"}


def test_create_duplicate_user(client: TestClient, create_user_in_db):
    # Directly create a user in the database using the fixture
    user = create_user_in_db(username="testuser", email="testuser@example.com")
    response = client.post("/users/", json={"username": user.username, "email": user.email})
    assert response.status_code == 400
    assert response.json()['detail'] == "Username already registered"


def test_update_user_success(client: TestClient, create_user_in_db):
    # Directly create a user in the database using the fixture
    user = create_user_in_db(username="testuser", email="testemail@mail.com")
    response = client.put(f"/users/{user.id}", json={"username": "newuser", "email": "newemail@email.com"})
    assert response.status_code == 200
    assert response.json() == {"username": "newuser", "id": user.id, "email": "newemail@email.com"}


def test_update_user_not_found(client: TestClient):
    response = client.put(f"/users/10", json={"username": "newuser", "email": "newemail@email.com"})
    assert response.status_code == 404
    assert response.json()['detail'] == "User not found"
