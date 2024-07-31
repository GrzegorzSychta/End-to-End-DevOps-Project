
import pytest
import random
import string
from flask import Flask
from ..backend.routes import bp
from ..backend.services import create_user
from ..backend.models import User
from ..backend.db import create_db_connection, disconnect
import time

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(bp)
    client = app.test_client()

    with app.app_context():
        create_db_connection("users")

    yield client

    with app.app_context():
        disconnect()

def test_create_user(client):
    first_name = 'Test'
    last_name = 'User'
    email = f'testuser{int(time.time())}@example.com'
    password = 'password123'

    create_user(first_name, last_name, email, password)

    user = User.objects(email=email).first()
    assert user is not None
    assert user.first_name == first_name
    assert user.last_name == last_name

def test_register_route(client):
    first_name = 'Test'
    last_name = 'User'
    email = f'testuser{int(time.time() * 1000)}@example.com'
    password = 'password123'
    data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password
    }

    response = client.post('/register', json=data)

    assert response.status_code == 201
    user = User.objects(email=data['email']).first()
    assert user is not None
    assert user.first_name == data['first_name']
    assert user.last_name == data['last_name']

def test_create_user_with_random_name(client):
    first_name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
    last_name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
    email = f'{first_name}.{last_name}@example.com'
    password = 'password123'

    create_user(first_name, last_name, email, password)

    user = User.objects(email=email).first()
    assert user is not None
    assert user.first_name == first_name
    assert user.last_name == last_name