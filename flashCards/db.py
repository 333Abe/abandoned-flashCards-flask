from flask import current_app, g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import click

db = SQLAlchemy()

def get_db():
    if 'db' not in g:
        echo_enabled = current_app.config.get('SQLALCHEMY_ECHO', False)
        g.db = db.create_engine(
            current_app.config['SQLALCHEMY_DATABASE_URI'],
            echo=echo_enabled
        )

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.dispose()

def init_db():
    db = get_db()
    with db.connect() as conn:

        with current_app.open_resource('schema.sql') as f:
            sql_script = f.read().decode('utf8')
        
        conn.execute(text(sql_script))
        conn.commit()


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)