from flask_login import login_user, logout_user
from flask import session
from .models import User
import secrets

def create_user(first_name, last_name, email, password):
    existing_user = User.objects(email=email).first()
    if existing_user:
        return {'error': 'A user with this email already exists.'}, 400

    user = User(first_name=first_name, last_name=last_name, email=email)
    user.set_password(password)
    user.save()
    return user

def login(email, password):
    user = User.objects(email=email).first()
    if user and user.check_password(password):
        login_user(user)
        return user
    else:
        return {'error': 'Invalid email or password.'}, 401

def load_user(user_id):
    return User.objects(id=user_id).first()

def set_secret_key(app):
    app.secret_key = secrets.token_hex(16)
    
def current_user():
    return session.get('user_id')

def is_authenticated():
    return current_user.is_authenticated if current_user else False

def is_active():
    return current_user.is_active if current_user else False

def get_current_user():
    return current_user if current_user else None

def logout():
    logout_user()

