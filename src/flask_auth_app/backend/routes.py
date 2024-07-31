from flask import Blueprint, request,  flash, jsonify
from flask_login import current_user
from .services import *
from .models import User

bp = Blueprint('routes', __name__)

@bp.route('/register', methods=['POST'])
def create_user_api():
    try:
        data = request.json
        print(f"Received data: {data}")  # Log the received data
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return jsonify({'error': 'Error parsing JSON.'}), 400

    try:
        user = create_user(data['first_name'], data['last_name'], data['email'], data['password'])
    except Exception as e:
        print(f"Error creating user: {e}")
        return jsonify({'error': 'Error creating user.'}), 500

    try:
        if isinstance(user, User):
            flash('User created successfully.')
            return jsonify({'message': 'User created successfully.'}), 201
        elif isinstance(user, tuple) and 'error' in user[0]:
            flash(user[0]['error'])
            return jsonify(user[0]), user[1]
        else:
            raise ValueError('Unexpected return value from create_user')
    except Exception as e:
        print(f"Error creating response: {e}")
        return jsonify({'error': 'Error creating response.'}), 500
    
@bp.route('/login', methods=['POST'])
def login_api():
    try:
        data = request.json
    except Exception as e:
        return jsonify({'error': 'Error parsing JSON.'}), 400

    try:
        user = login(data['email'], data['password'])
    except Exception as e:
        return jsonify({'error': 'Error logging in user.'}), 500

    try:
        if isinstance(user, User):
            return jsonify({'message': 'User logged in successfully.'}), 200
        elif isinstance(user, tuple) and 'error' in user[0]:
            return jsonify(user[0]), user[1]
        else:
            raise ValueError('Unexpected return value from login')
    except Exception as e:
        return jsonify({'error': 'Error creating response.'}), 500

@bp.route('/logout', methods=['POST'])
def logout_api():
    try:
        logout()
        return jsonify({'message': 'User logged out successfully.'}), 200
    except Exception as e:
        return jsonify({'error': 'Error logging out user.'}), 500
    
