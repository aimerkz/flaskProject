from flask import request
from flask_restful import Resource
from api.models import FileInformartion, db


class FileInfo(Resource):
    def get(self):
        files = FileInformartion.query.all()
        if files:
            return {'files': list(file.json() for file in files)}
        else:
            return {'message': 'Objects not found'}

    def post(self):
        data = request.get_json()
        new_file = FileInformartion(
            data['name'],
            data['extension'],
            data['size'],
            data['path'],
            data['created_at'],
            data['updated_at'],
            data['comment']
        )
        db.session.add(new_file)
        db.session.commit()
        return new_file.json(), 201
