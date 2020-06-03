from app import db


class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_URL = db.Column(db.String(), unique=True, nullable=True)
    short_URL = db.Column(db.String(), unique=True, nullable=True)
    
    def __repr__(self):
        return '<ID {}>'.format(self.id)