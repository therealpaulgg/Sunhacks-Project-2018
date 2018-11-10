# Data classes for the app

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Restaurant - make a request to google maps API and then get the data back and return it as json to vue

class Restaurant(db.Model):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            questions=[question.to_dict() for question in self.questions]
        )


# User

# Restaurants Visited

# Points
