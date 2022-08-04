from enum import unique
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class Cow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(10), unique=True)
    breed = db.Column(db.String(15), nullable=False)


    def __repr__(self) -> str:
        return f"Cow: {self.tag}"


class CowSchema(ma.Schema):
    class Meta:
        fields = ('id', 'tag', 'breed')