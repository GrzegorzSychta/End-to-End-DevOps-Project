import os

DB_NAME = os.getenv('DB_NAME')

DB_HOST = os.getenv('DB_HOST')

DB_PORT = int(os.getenv('DB_PORT'))

DB_USER = os.getenv('DB_USER')

DB_PASSWORD = os.getenv('DB_PASSWORD')

DB_AUTH_SOURCE = os.getenv('DB_AUTH_SOURCE')

DB_CA_FILE = os.getenv('DB_CA_FILE')