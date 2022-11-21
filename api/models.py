from _datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class FileInformartion(db.Model):
    __tablename__ = 'file_information'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    extension = db.Column(db.String(10), nullable=False)
    size = db.Column(db.Integer)
    path = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_ad = db.Column(db.DateTime, nullable=True)
    comment = db.Column(db.Text)
