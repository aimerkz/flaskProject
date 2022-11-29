from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint

from api.models import db
from api.views import FileUpload, FileList, FileDetail, FileSearch, FileDownload


app = Flask(__name__)
app.config.from_object('flaskProject.config.Config')

api = Api(app)
db.init_app(app)
migrate = Migrate(app, db)

# swagger config
SWAGGER_URL = '/api/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUERPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'flask Project API'
    }
)
app.register_blueprint(SWAGGER_BLUERPRINT, url_prefix=SWAGGER_URL)

api.add_resource(FileList, '/api/files/')
api.add_resource(FileDetail, '/api/files/<int:file_id>/')
api.add_resource(FileSearch, '/api/files/search/')
api.add_resource(FileUpload, '/api/files/upload/')
api.add_resource(FileDownload, '/api/files/<int:file_id>/download/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
