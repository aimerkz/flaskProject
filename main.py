from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from api.models import db
from api.views import FileList, FileDetail


app = Flask(__name__)
app.config.from_object('flaskProject.config.Config')

api = Api(app)
db.init_app(app)
migrate = Migrate(app, db)

api.add_resource(FileList, '/api/files/')
api.add_resource(FileDetail, '/api/files/<int:file_id>/')

if __name__ == '__main__':
    app.run()
