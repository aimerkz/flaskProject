from flask import request
from flask_restful import Resource
from api.models import File, db


class FileList(Resource):
    """Получение списка всех файлов. Создание файла."""
    def get(self):
        files = File.query.all()
        if files:
            return {'files': list(file.json() for file in files)}
        else:
            return {'message': 'Objects not found'}, 404

    def post(self):
        data = request.get_json()
        new_file = File(
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


class FileDetail(Resource):
    """Получение файла по file_id. Удаление файла."""
    def get(self, file_id):
        file = File.query.filter_by(file_id=file_id).first_or_404()
        return file.json()

    def delete(self, file_id):
        file = File.query.filter_by(file_id=file_id).first_or_404()
        db.session.delete(file)
        db.session.commit()
        return {'message': 'File deleted successfully'}, 204


class FileSearch(Resource):
    """Получение списка всех файлов с учетом поиска по path."""
    def get(self, *args, **kwargs):
        args = request.args
        files = File.query.filter(File.path.ilike('%'+args.get('path')+'%')).all()
        if files:
            return {'files': list(file.json() for file in files)}
        else:
            return {'message': 'Objects not found'}, 404
