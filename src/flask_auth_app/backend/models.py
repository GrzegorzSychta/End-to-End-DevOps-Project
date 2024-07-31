from mongoengine import Document, StringField, BooleanField, EmailField
from werkzeug.security import generate_password_hash, check_password_hash

class User(Document):
    password_hash = StringField(required=True)
    active = BooleanField(default=True)
    email = EmailField(required=True, unique=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return self.active

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)