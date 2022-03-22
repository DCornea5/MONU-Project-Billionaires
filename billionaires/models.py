# from tokenize import Name
from .app import db


class Billionaires(db.Model):
    __tablename__ = 'billionaires'

    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64))
    Country = db.Column(db.String)
    geometry = db.Column(db.String)
    NetWorth = db.Column(db.Float)
    Age = db.Column(db.Float)
    Source = db.Column(db.String)
    Rank = db.Column(db.Float)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    Counts = db.Column(db.Float)
    def __repr__(self):
        return '<Billionaires %r>' % (self.name)


       

