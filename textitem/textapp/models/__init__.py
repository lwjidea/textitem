from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# from .text import Text

def init_db(app):
    db.init_app(app=app)