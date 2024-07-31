from mongoengine import Document, StringField, FloatField, DateTimeField, ReferenceField
from datetime import datetime

class Expense(Document):
    name = StringField(required=True, max_length=200)
    amount = FloatField(required=True)
    description = StringField(max_length=500)
    date = DateTimeField(required=True)
    category = StringField(max_length=200)

    def to_json(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'amount': self.amount,
            'description': self.description,
            'date': self.date.isoformat(),
            'category': self.category
        }


