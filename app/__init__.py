from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.model import URLs

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)
""" db.create_all()
db.session.commit() #added  """

from app import routes