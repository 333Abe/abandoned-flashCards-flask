from flask import current_app, g
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def get_db():
    if 'db' not in g:
        g.db = db.create_engine(
            current_app.config['SQLALCHEMY_DATABASE_URI'],
            echo=current_app.config['SQLALCHEMY_ECHO']
        )

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.dispose()