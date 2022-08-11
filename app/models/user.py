from datetime import datetime

import pytz
from dateutil.tz import tzutc

from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    father = db.Column(db.String(256), nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now(),)

    def __init__(self, name,father):
        self.name = name
        self.father=father
        self.timestamp = datetime.utcnow()


    def serialize(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'created_at': str(self.timestamp),

        }

    def save(self):
        db.session.add(self)
        db.session.commit()
