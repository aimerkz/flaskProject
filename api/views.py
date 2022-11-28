import os
from os.path import join, dirname, realpath
import json

from flask import request
from flask_restful import Resource
from api.models import File, db
from werkzeug.utils import secure_filename


UPLOAD_PATH = join(dirname(realpath(__file__)), '../static/uploads/')


class FileUpload(Resource):
    """Загрузка файла из локального хранилища."""
    def post(self):
        file = request.files.get('file')
        data = request.args.get('comment')
        filename = secure_filename(file.filename)
        upload = File(
            name='.'.join(filename.split('.')[:-1]),
            extension='.'+'.'.join(filename.split('.')[-1:]),
            size=(os.stat(filename)).st_size,
            path=UPLOAD_PATH,
            created_at=None,
            updated_at=None,
            comment=data
        )
        file.save(os.path.join(UPLOAD_PATH, filename))
        db.session.add(upload)
        db.session.commit()
        return 'File uploaded successfully', 201


class FileList(Resource):
    """Получение списка всех файлов. Создание информации о файле."""
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
        files = File.query.filter(File.path.ilike('%' + args.get('path') + '%')).all()
        if files:
            return {'files': list(file.json() for file in files)}
        else:
            return {'message': 'Objects not found'}, 404
