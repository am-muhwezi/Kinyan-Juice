import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models.users_db_model import User

import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from app import create_app, db


@pytest.fixture
def client():
    app = create_app("testing")  # Ensure your app supports a testing config
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

def test_signup(client):
    response = client.post("/auth/signup", json={
        "email": "test@example.com",
        "password": "password123"
    })
    assert response.status_code == 201

def test_login(client):
    user = User(email="test@example.com")
    user.set_password("password123")
    db.session.add(user)
    db.session.commit()

    response = client.post("/auth/login", json={
        "email": "test@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert "access_token" in response.get_json()

def test_protected_route(client):
    token = create_access_token(identity="test@example.com")
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/products/products", headers=headers)
    assert response.status_code == 200
