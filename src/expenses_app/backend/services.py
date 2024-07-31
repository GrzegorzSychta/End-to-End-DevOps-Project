from .models import *
from datetime import datetime
from mongoengine import DoesNotExist

# GET

def get_expenses():
    return [expense.to_json() for expense in Expense.objects.all()]

def get_expense(id):
    return Expense.objects.get(id=id).to_json()

def get_expenses_by_name(name):
    expenses = Expense.objects(name=name)
    return [expense.to_json() for expense in expenses]

def get_expenses_by_category(category):
    expenses = Expense.objects(category=category)
    return [expense.to_json() for expense in expenses]

def get_expenses_by_date_range(start_date, end_date):
    expenses = Expense.objects(date__gte=start_date, date__lte=end_date)
    return [expense.to_json() for expense in expenses]

def get_expenses_by_name_and_date_range(name, start_date, end_date):
    expenses = Expense.objects(name=name, date__gte=start_date, date__lte=end_date)
    return [expense.to_json() for expense in expenses]

def get_expenses_by_name_and_category(name, category):
    expenses = Expense.objects(name=name, category=category)
    return [expense.to_json() for expense in expenses]

def get_expenses_by_category_and_date_range(category, start_date, end_date):
    expenses = Expense.objects(category=category, date__gte=start_date, date__lte=end_date)
    return [expense.to_json() for expense in expenses]

def get_expenses_by_name_and_category_and_date_range(name, category, start_date, end_date):
    expenses = Expense.objects(name=name, category=category, date__gte=start_date, date__lte=end_date)
    return [expense.to_json() for expense in expenses]

# ADD

def add_amount_to_expense(expense_id, amount):
    expense = Expense.objects.get(id=expense_id)
    expense.amount += amount
    expense.save()

# SUBTRACT

def subtract_amount_from_expense(expense_id, amount):
    expense = Expense.objects.get(id=expense_id)
    expense.amount -= amount
    expense.save()

# CREATE

def add_expense(data):
    if isinstance(data['date'], str):
        data['date'] = datetime.strptime(data['date'], '%Y-%m-%d')
    expense = Expense(**data)
    expense.save()
    return expense.to_json()

# UPDATE

def update_expense(id, data):
    try:
        expense = Expense.objects.get(id=id)
    except DoesNotExist:
        return None
    
    for key, value in data.items():
        if key == 'date':
            # Convert string date to datetime object
            value = datetime.strptime(value, '%Y-%m-%d')
        setattr(expense, key, value)
    
    expense.save()
    return expense.to_json()

def update_expense_name(id, name):
    Expense.objects(id=id).update(name=name)
    return Expense.objects.get(id=id).to_json()

def update_expense_category(id, category):
    Expense.objects(id=id).update(category=category)
    return Expense.objects.get(id=id).to_json()

def update_expense_description(id, description):
    Expense.objects(id=id).update(description=description)
    return Expense.objects.get(id=id).to_json()

def update_expense_date(id, date):
    Expense.objects(id=id).update(date=date)
    return Expense.objects.get(id=id).to_json()

def update_expense_amount(id, amount):
    Expense.objects(id=id).update(amount=amount)
    return Expense.objects.get(id=id).to_json()

# DELETE

def delete_expense(id):
    Expense.objects.get(id=id).delete()

def delete_expenses_by_name(name):
    Expense.objects(name=name).delete()
    return '', 204

def delete_expenses_by_category(category):
    Expense.objects(category=category).delete()
    return '', 204

def delete_expenses_by_date_range(start_date, end_date):
    Expense.objects(date__gte=start_date, date__lte=end_date).delete()
    return '', 204

