from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Player(db.Model):
    id = db.Column(db.Integer, primaryKey=True)
    creation_Date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Player id: {self.id}>'

