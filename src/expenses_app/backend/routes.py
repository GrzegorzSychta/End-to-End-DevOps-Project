from flask import Blueprint, request, jsonify, g
from mongoengine import ValidationError
from .db import create_db_connection
from .models import *
from .services import *

bp = Blueprint('routes', __name__)

@bp.before_request
def before_request():
    g.db = create_db_connection()

@bp.route('/expenses', methods=['GET'])
def get_expenses_route():
    return jsonify(get_expenses()), 200

@bp.route('/expenses/<id>', methods=['GET'])
def get_expense_route(id):
    return jsonify(get_expense(id)), 200

@bp.route('/expenses/name/<name>', methods=['GET'])
def get_expenses_by_name_route(name):
    return jsonify(get_expenses_by_name(name)), 200

@bp.route('/expenses/category/<category>', methods=['GET'])
def get_expenses_by_category_route(category):
    return jsonify(get_expenses_by_category(category)), 200

@bp.route('/expenses/date_range', methods=['GET'])
def get_expenses_by_date_range_route():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    return jsonify(get_expenses_by_date_range(start_date, end_date)), 200

@bp.route('/expenses/name/<name>/category/<category>', methods=['GET'])
def get_expenses_by_name_and_category_route(name, category):
    return jsonify(get_expenses_by_name_and_category(name, category)), 200

@bp.route('/expenses', methods=['POST'])
def add_expense_route():
    return jsonify(add_expense(request.json)), 201

@bp.route('/expenses/<id>', methods=['PUT'])
def update_expense_route(id):
    return jsonify(update_expense(id, request.json)), 200

@bp.route('/expenses/<id>', methods=['DELETE'])
def delete_expense_route(id):
    delete_expense(id)
    return '', 204

@bp.route('/expenses/name/<name>/delete', methods=['DELETE'])
def delete_expenses_by_name_route(name):
    delete_expenses_by_name(name)
    return '', 204

@bp.route('/expenses/category/<category>/delete', methods=['DELETE'])
def delete_expenses_by_category_route(category):
    delete_expenses_by_category(category)
    return '', 204