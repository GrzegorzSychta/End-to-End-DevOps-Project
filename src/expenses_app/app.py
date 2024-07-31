from flask import Flask
from .backend.db import create_db_connection
from .backend.routes import bp
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

create_db_connection()

app.register_blueprint(bp)

if __name__ == '__main__':
    app.run()