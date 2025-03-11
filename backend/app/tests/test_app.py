# test_app.py - Unittest Style Tests
import unittest
import json
import sys
import os
from app import create_app, db
from app.models.users_db_model import User



class FlaskAppTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        """Set up test environment before each test"""
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        
        with self.app.app_context():
            db.create_all()
            
    def tearDown(self):
        """Clean up after each test"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
    
    def test_index_route(self):
        """Test the index route returns 200 status"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_create_user(self):
        """Test user creation endpoint"""
        response = self.client.post(
            '/api/users',
            data=json.dumps({'username': 'testuser', 'email': 'test@example.com'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['username'], 'testuser')
        
    def test_get_user(self):
        """Test getting a user by ID"""
        # First create a user
        self.client.post(
            '/api/users',
            data=json.dumps({'username': 'testuser', 'email': 'test@example.com'}),
            content_type='application/json'
        )
        
        # Then retrieve the user
        response = self.client.get('/api/users/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['username'], 'testuser')
    
    def test_update_user(self):
        """Test updating a user"""
        # First create a user
        self.client.post(
            '/api/users',
            data=json.dumps({'username': 'testuser', 'email': 'test@example.com'}),
            content_type='application/json'
        )
        
        # Then update the user
        response = self.client.put(
            '/api/users/1',
            data=json.dumps({'username': 'updateduser', 'email': 'updated@example.com'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['username'], 'updateduser')
    
    def test_delete_user(self):
        """Test deleting a user"""
        # First create a user
        self.client.post(
            '/api/users',
            data=json.dumps({'username': 'testuser', 'email': 'test@example.com'}),
            content_type='application/json'
        )
        
        # Then delete the user
        response = self.client.delete('/api/users/1')
        self.assertEqual(response.status_code, 204)
        
        # Verify user is deleted
        response = self.client.get('/api/users/1')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()


# test_app_pytest.py - Pytest Style Tests
import pytest
import json
from app import create_app, db
from app.models.users_db_model import User  # Adjust this import based on your actual models

@pytest.fixture
def client():
    """Create a test client for the app"""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        
    with app.test_client() as client:
        yield client
        
    with app.app_context():
        db.session.remove()
        db.drop_all()

def test_index_route(client):
    """Test the index route returns 200 status"""
    response = client.get('/')
    assert response.status_code == 200

def test_create_user(client):
    """Test user creation endpoint"""
    response = client.post(
        '/api/users',
        data=json.dumps({'username': 'testuser', 'email': 'test@example.com'}),
        content_type='application/json'
    )
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['username'] == 'testuser'

def test_get_user(client):
    """Test getting a user by ID"""
    # First create a user
    client.post(
        '/api/users',
        data=json.dumps({'username': 'testuser', 'email': 'test@example.com'}),
        content_type='application/json'
    )
    
    # Then retrieve the user
    response = client.get('/api/users/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['username'] == 'testuser'

def test_update_user(client):
    """Test updating a user"""
    # First create a user
    client.post(
        '/api/users',
        data=json.dumps({'username': 'testuser', 'email': 'test@example.com'}),
        content_type='application/json'
    )
    
    # Then update the user
    response = client.put(
        '/api/users/1',
        data=json.dumps({'username': 'updateduser', 'email': 'updated@example.com'}),
        content_type='application/json'
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['username'] == 'updateduser'

def test_delete_user(client):
    """Test deleting a user"""
    # First create a user
    client.post(
        '/api/users',
        data=json.dumps({'username': 'testuser', 'email': 'test@example.com'}),
        content_type='application/json'
    )
    
    # Then delete the user
    response = client.delete('/api/users/1')
    assert response.status_code == 204
    
    # Verify user is deleted
    response = client.get('/api/users/1')
    assert response.status_code == 404


# conftest.py - Additional Pytest Configuration
import pytest
from app import create_app, db

@pytest.fixture(scope='session')
def app_context():
    """Create application context for tests"""
    with app.app_context():
        yield

@pytest.fixture(scope='function')
def sample_user(app_context):
    """Create a sample user for testing"""
    from models import User  # Import here to avoid circular imports
    user = User(username='sampleuser', email='sample@example.com')
    db.session.add(user)
    db.session.commit()
    
    yield user
    
    db.session.delete(user)
    db.session.commit()
