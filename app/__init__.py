from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from app.model import URLs

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shorturl.db'
db = SQLAlchemy(app)

from app import routes

# class URL(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     url = db.Column(db.String(), unique=True, nullable=False)

#     def __repr__(self):
#         return '<ID {}>'.format(self.id)

# db.app=app
# # db.create_all()
# db.session.commit()

