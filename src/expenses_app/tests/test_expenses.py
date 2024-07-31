import pytest
from expenses.backend.services import *
from expenses.backend.models import Expense
from expenses.backend.db import create_db_connection
from unittest.mock import patch
import mongomock
import random
import json
from datetime import datetime
import mongoengine.errors

# Sample data

expenses_data = [
    {'amount': 100.0, 'description': 'Grocerries', 'date': '2022-01-01', 'name': 'Expense Name 1', 'category': 'Test Category 1'},
    {'amount': 200.0, 'description': 'Test Expense 2', 'date': '2022-01-02', 'name': 'Expense Name 2', 'category': 'Whatever Category 2'},
    {'amount': 300.0, 'description': 'Test Expense 2', 'date': '2023-01-05', 'name': 'Expense Name 2', 'category': 'Test Category 2'},
    {'amount': 50.0, 'description': '', 'date': '2025-01-02', 'name': 'Expense Name 2', 'category': ''},
    {'amount': 1.0, 'description': 'Test Expense 2', 'date': '2021-01-02', 'name': 'Expense Name 2', 'category': 'Test Category 2'},

]

@pytest.fixture(scope='module')
def db():
    with patch('pymongo.MongoClient', new=mongomock.MongoClient):
        db = create_db_connection(db_name='test_db')  # Use a separate test database
        yield db

@pytest.fixture(scope='function')
def populate_db(db):
    Expense.objects.all().delete()  # Clear the database before each test
    for expense_data in expenses_data:
        Expense(**expense_data).save()

# GET

def test_get_expenses(populate_db):
    expenses = get_expenses()
    assert len(expenses) == len(expenses_data)
    for i in range(len(expenses)):
        assert expenses[i]['amount'] == expenses_data[i]['amount']
        assert expenses[i]['description'] == expenses_data[i]['description']
        assert expenses[i]['name'] == expenses_data[i]['name']
        assert expenses[i]['category'] == expenses_data[i]['category']

def test_get_expense(populate_db):
    mock_expense_data = random.choice(expenses_data)
    mock_expense_id = Expense(**mock_expense_data).save().id
    expense = get_expense(mock_expense_id)
    assert expense['amount'] == mock_expense_data['amount']
    assert expense['description'] == mock_expense_data['description']
    assert expense['name'] == mock_expense_data['name']
    assert expense['category'] == mock_expense_data['category']

def test_get_expenses_by_name(populate_db):
    mock_expense_name = random.choice(expenses_data)['name']
    expenses = get_expenses_by_name(mock_expense_name)
    mock_expenses = [expense for expense in expenses_data if expense['name'] == mock_expense_name]
    assert len(expenses) == len(mock_expenses)
    for i in range(len(expenses)):
        assert expenses[i]['amount'] == mock_expenses[i]['amount']
        assert expenses[i]['description'] == mock_expenses[i]['description']
        assert expenses[i]['name'] == mock_expenses[i]['name']
        assert expenses[i]['category'] == mock_expenses[i]['category']

def test_get_expenses_by_category(populate_db):
    mock_expense_category = random.choice(expenses_data)['category']
    expenses = get_expenses_by_category(mock_expense_category)
    mock_expenses = [expense for expense in expenses_data if expense['category'] == mock_expense_category]
    assert len(expenses) == len(mock_expenses)
    for i in range(len(expenses)):
        assert expenses[i]['amount'] == mock_expenses[i]['amount']
        assert expenses[i]['description'] == mock_expenses[i]['description']
        assert expenses[i]['name'] == mock_expenses[i]['name']
        assert expenses[i]['category'] == mock_expenses[i]['category']

def test_get_expenses_by_date_range(populate_db):
    start_date = min(expense['date'] for expense in expenses_data)
    end_date = max(expense['date'] for expense in expenses_data)
    expenses = get_expenses_by_date_range(start_date, end_date)
    mock_expenses = [expense for expense in expenses_data if start_date <= expense['date'] <= end_date]
    assert len(expenses) == len(mock_expenses)
    for i in range(len(expenses)):
        assert expenses[i]['amount'] == mock_expenses[i]['amount']
        assert expenses[i]['description'] == mock_expenses[i]['description']
        assert expenses[i]['name'] == mock_expenses[i]['name']
        assert expenses[i]['category'] == mock_expenses[i]['category']

def test_get_expenses_by_name_and_date_range(populate_db):
    mock_expense_name = random.choice(expenses_data)['name']
    start_date = min(expense['date'] for expense in expenses_data)
    end_date = max(expense['date'] for expense in expenses_data)
    expenses = get_expenses_by_name_and_date_range(mock_expense_name, start_date, end_date)
    mock_expenses = [expense for expense in expenses_data if expense['name'] == mock_expense_name and start_date <= expense['date'] <= end_date]
    assert len(expenses) == len(mock_expenses)
    for i in range(len(expenses)):
        assert expenses[i]['amount'] == mock_expenses[i]['amount']
        assert expenses[i]['description'] == mock_expenses[i]['description']
        assert expenses[i]['name'] == mock_expenses[i]['name']
        assert expenses[i]['category'] == mock_expenses[i]['category']

def test_get_expenses_by_nonexistent_category(populate_db):
    expenses = get_expenses_by_category('Nonexistent Category')
    assert len(expenses) == 0

def test_get_expenses_by_invalid_date_range(populate_db):
    start_date = max(expense['date'] for expense in expenses_data)
    end_date = min(expense['date'] for expense in expenses_data)
    expenses = get_expenses_by_date_range(start_date, end_date)
    assert len(expenses) == 0

def test_get_expenses_by_empty_category(populate_db):
    expenses = get_expenses_by_category('')
    mock_expenses = [expense for expense in expenses_data if expense['category'] == '']
    assert len(expenses) == len(mock_expenses)

def test_get_expenses_by_date_range_in_future(populate_db):
    future_date = '2030-01-01'
    expenses = get_expenses_by_date_range(future_date, future_date)
    assert len(expenses) == 0

def test_get_expenses_by_name_and_date_range_with_nonexistent_name(populate_db):
    nonexistent_name = 'Nonexistent Name'
    start_date = min(expense['date'] for expense in expenses_data)
    end_date = max(expense['date'] for expense in expenses_data)
    expenses = get_expenses_by_name_and_date_range(nonexistent_name, start_date, end_date)
    assert len(expenses) == 0

def test_get_expenses_by_name_and_date_range_with_empty_name(populate_db):
    empty_name = ''
    start_date = min(expense['date'] for expense in expenses_data)
    end_date = max(expense['date'] for expense in expenses_data)
    expenses = get_expenses_by_name_and_date_range(empty_name, start_date, end_date)
    mock_expenses = [expense for expense in expenses_data if expense['name'] == empty_name and start_date <= expense['date'] <= end_date]
    assert len(expenses) == len(mock_expenses)

# ADD
    
def test_add_amount_to_expense(populate_db):
    mock_expense_data = random.choice(expenses_data)
    mock_expense_id = Expense(**mock_expense_data).save().id
    original_amount = mock_expense_data['amount']
    amount_to_add = random.randint(1, 100)
    add_amount_to_expense(mock_expense_id, amount_to_add)
    updated_expense = Expense.objects.get(id=mock_expense_id)
    assert updated_expense['amount'] == original_amount + amount_to_add

# SUBTRACT
    
def test_subtract_amount_from_expense(populate_db):
    mock_expense_data = random.choice(expenses_data)
    mock_expense_id = Expense(**mock_expense_data).save().id
    original_amount = mock_expense_data['amount']
    amount_to_subtract = random.randint(1, 100)
    subtract_amount_from_expense(mock_expense_id, amount_to_subtract)
    updated_expense = Expense.objects.get(id=mock_expense_id)
    assert updated_expense['amount'] == original_amount - amount_to_subtract

# CREATE

def test_add_expense(populate_db):
    new_expense_data = {'amount': 400.0, 'description': 'Test Expense 4', 'date': datetime(2022, 2, 2), 'name': 'Expense Name 4', 'category': 'Test Category 4'}
    added_expense = add_expense(new_expense_data)
    assert added_expense['amount'] == new_expense_data['amount']
    assert added_expense['description'] == new_expense_data['description']
    assert added_expense['name'] == new_expense_data['name']
    assert added_expense['category'] == new_expense_data['category']
    assert added_expense['date'] == new_expense_data['date'].isoformat()
    assert Expense.objects.get(id=added_expense['id']) is not None

# UPDATE
    
def test_update_expense(populate_db):
    mock_expense_data = random.choice(expenses_data)
    mock_expense_id = Expense(**mock_expense_data).save().id
    update_data = {'amount': 500.0, 'description': 'Updated Expense', 'date': datetime(2022, 3, 3), 'name': 'Updated Name', 'category': 'Updated Category'}
    updated_expense = update_expense(mock_expense_id, update_data)
    assert updated_expense['id'] == str(mock_expense_id)
    assert updated_expense['amount'] == update_data['amount']
    assert updated_expense['description'] == update_data['description']
    assert updated_expense['name'] == update_data['name']
    assert updated_expense['category'] == update_data['category']

def test_update_expense_description(populate_db):
    mock_expense_data = random.choice(expenses_data)
    mock_expense_id = Expense(**mock_expense_data).save().id
    new_description = 'Updated Description'
    update_expense_description(str(mock_expense_id), new_description)
    updated_expense = Expense.objects.get(id=mock_expense_id)
    assert updated_expense.description == new_description

def test_update_expense_description_nonexistent_id(populate_db):
    nonexistent_id = '65b8d65e2efbd9194d8b47d1'  # Solenoid
    new_description = 'Updated Description'
    with pytest.raises(DoesNotExist):
        update_expense_description(nonexistent_id, new_description)

def test_update_expense_description_empty_string(populate_db):
    mock_expense_data = random.choice(expenses_data)
    mock_expense_id = Expense(**mock_expense_data).save().id
    new_description = ''
    update_expense_description(str(mock_expense_id), new_description)
    updated_expense = Expense.objects.get(id=mock_expense_id)
    assert updated_expense.description == new_description

# DELETE
    
def test_delete_expense(populate_db):
    mock_expense_data = random.choice(expenses_data)
    mock_expense_id = Expense(**mock_expense_data).save().id
    delete_expense(str(mock_expense_id))
    with pytest.raises(DoesNotExist):
        Expense.objects.get(id=mock_expense_id)

def test_delete_expense_nonexistent_id(populate_db):
    nonexistent_id = '65b8d65e2efbd9194d8b47d1'
    with pytest.raises(DoesNotExist):
        delete_expense(nonexistent_id)

def test_delete_expenses_by_name(populate_db):
    mock_expense_name = random.choice(expenses_data)['name']
    delete_expenses_by_name(mock_expense_name)
    deleted_expenses = Expense.objects(name=mock_expense_name)
    assert len(deleted_expenses) == 0

def test_delete_expenses_by_nonexistent_name(populate_db):
    nonexistent_name = '65random_name31'
    delete_expenses_by_name(nonexistent_name)
    deleted_expenses = Expense.objects(name=nonexistent_name)
    assert len(deleted_expenses) == 0

def test_delete_expenses_by_category(populate_db):
    mock_expense_category = random.choice(expenses_data)['category']
    delete_expenses_by_category(mock_expense_category)
    deleted_expenses = Expense.objects(category=mock_expense_category)
    assert len(deleted_expenses) == 0

def test_delete_expenses_by_nonexistent_category(populate_db):
    nonexistent_category = '65random_name31' 
    delete_expenses_by_category(nonexistent_category)
    deleted_expenses = Expense.objects(category=nonexistent_category)
    assert len(deleted_expenses) == 0

def test_delete_expenses_by_date_range(populate_db):
    start_date = min(expense['date'] for expense in expenses_data)
    end_date = max(expense['date'] for expense in expenses_data)
    delete_expenses_by_date_range(start_date, end_date)
    deleted_expenses = Expense.objects(date__gte=start_date, date__lte=end_date)
    assert len(deleted_expenses) == 0

def test_delete_expenses_by_nonexistent_date_range(populate_db):
    start_date = '3000-01-01'
    end_date = '4000-01-01'
    delete_expenses_by_date_range(start_date, end_date)
    deleted_expenses = Expense.objects(date__gte=start_date, date__lte=end_date)
    assert len(deleted_expenses) == 0