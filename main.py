import os

from dotenv import load_dotenv

from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from api.models import db
from api.views import FileList, FileDetail


load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('TRACK_MODIFICATIONS')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

api = Api(app)
db.init_app(app)
migrate = Migrate(app, db)

api.add_resource(FileList, '/api/files/')
api.add_resource(FileDetail, '/api/files/<int:file_id>/')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')
