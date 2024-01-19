from flask import current_app, g
from flask_sqlalchemy import SQLAlchemy
import click

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

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)