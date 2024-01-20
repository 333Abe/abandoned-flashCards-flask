from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from sqlalchemy import select


from flashCards.db import get_db

bp = Blueprint('select_topics', __name__)

@bp.route('/')
def index():
    db = get_db()
    statement = select(cards.topic)
    with db.connect as conn:
        topics = conn.execute(statement)
        print(topics.unique())