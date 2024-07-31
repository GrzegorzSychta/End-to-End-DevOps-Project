from flask import Flask
from flask_login import LoginManager
from flask_cors import CORS
from .backend.db import create_db_connection, disconnect
from .backend.routes import bp
from .backend.services import load_user, set_secret_key

app = Flask(__name__)

CORS(app)

login_manager = LoginManager(app)

@app.before_request
def before_request():
    create_db_connection("users")

@app.teardown_request
def teardown_db(exception=None):
    disconnect()

@login_manager.user_loader
def user_loader(user_id):
    return load_user(user_id)

set_secret_key(app)

app.register_blueprint(bp)

if __name__ == '__main__':
    app.run
