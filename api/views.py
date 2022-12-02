import datetime
import os
import shutil
import io

from os.path import join, dirname, realpath

from flask import request, current_app, send_file, render_template, make_response
from flask_restful import Resource
from api.models import File, db
from flaskProject.filename_config import secure_filename


PARENT_DIR = os.path.dirname(os.path.abspath(__file__)).replace('api', '')
UPLOAD_DIR = join(dirname(realpath(PARENT_DIR)), 'flaskProject/static/uploads/')


class FileUpload(Resource):
    """Загрузка файла из локального хранилища"""
    def post(self):
        file = request.files.get('file')
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_DIR, filename))
        upload = File(
            name='.'.join(filename.split('.')[:-1]),
            extension='.' + '.'.join(filename.split('.')[-1:]),
            size=os.path.getsize(UPLOAD_DIR + filename),
            path=UPLOAD_DIR,
            created_at=None,
            updated_at=None,
            comment=None
        )
        db.session.add(upload)
        db.session.commit()
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('upload_done.html'), 201,
                             headers)


class FileUploadForm(Resource):
    """Загрузка файла через форму HTML"""
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('upload_file.html'), 200,
                             headers)


class FileDownload(Resource):
    """Скачивание файла по file_id"""
    def get(self, file_id):
        file = File.query.filter_by(file_id=file_id).first_or_404()
        uploads = os.path.join(current_app.root_path, UPLOAD_DIR)
        with open(uploads + (file.name + file.extension), 'rb') as f:
            file_download = f.read()
        output = io.BytesIO()
        output.write(file_download)
        output.seek(0)
        response = send_file(
            output,
            as_attachment=True,
            download_name=file.name + file.extension,
        )
        return response


class FileListCreate(Resource):
    """Получение списка всех файлов. Создание информации о файле"""
    def get(self):
        files = File.query.all()
        if files:
            return {'files': list(file.json() for file in files)}
        else:
            return 'Objects not found', 404

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
    """Получение файла по file_id. Обновление файла. Удаление файла"""
    def get(self, file_id):
        file = File.query.filter_by(file_id=file_id).first_or_404()
        return file.json()

    def put(self, file_id):
        data = request.get_json()
        file = File.query.filter_by(file_id=file_id).first_or_404()
        old_name = file.path + file.name + file.extension
        file.name = data['name']
        file.path = data['path']
        file.comment = data['comment']
        file.updated_at = datetime.datetime.now()
        db.session.commit()
        new_name = file.path + file.name + file.extension
        shutil.move(old_name, new_name)
        return 'File information updated successfully'

    def delete(self, file_id):
        file = File.query.filter_by(file_id=file_id).first_or_404()
        os.remove(file.path + file.name + file.extension)
        db.session.delete(file)
        db.session.commit()
        return 'File deleted successfully', 204


class FileSearch(Resource):
    """Получение списка всех файлов с учетом поиска по path"""
    def get(self, *args, **kwargs):
        args = request.args
        files = File.query.filter(File.path.ilike('%' + args.get('path') + '%')).all()
        if files:
            return {'files': list(file.json() for file in files)}
        else:
            return 'Objects not found', 404
