from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class File(db.Model):
    __tablename__ = 'file'

    file_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    extension = db.Column(db.String(10), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    path = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=True)
    comment = db.Column(db.Text, nullable=True)

    def __init__(self, name, extension, size, path,
                 created_at, updated_at, comment):
        self.name = name
        self.extension = extension
        self.size = size
        self.path = path
        self.created_at = created_at
        self.updated_at = updated_at
        self.comment = comment

    def json(self):
        return {'name': self.name, 'extension': self.extension,
                'size': self.size, 'path': self.path,
                'created_at': str(self.created_at), 'updated_at': str(self.updated_at),
                'comment': self.comment}
