from mongoengine import connect
from .. import config

def create_db_connection(db_name=None):
    if db_name is None:
        db_name = config.DB_NAME

    client = connect(
        db=db_name,
        host=config.DB_HOST,
        port=config.DB_PORT,
        username=config.DB_USER,
        password=config.DB_PASSWORD,
        authentication_source=config.DB_AUTH_SOURCE,
        tls=True,
        tlsCAFile=config.DB_CA_FILE
    )
    return client
