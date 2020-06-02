from app import db


class URLs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(), unique=True, nullable=False)

    def __repr__(self):
        return '<ID {}>'.format(self.id)