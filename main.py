import os

from flask import Flask
from flask_restful import Api

from api.models import db
from api.views import FileInfo


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('TRACK_MODIFICATIONS')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
api = Api()
db.init_app(app)

api.add_resource(FileInfo, '/api/files/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5000, host='127.0.0.1')
