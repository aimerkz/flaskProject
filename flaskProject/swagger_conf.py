from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)


SWAGGER_URL = '/api/swagger/'
API_URL = 'http://127.0.0.1:3000'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'FlaskTestProject': 'Test'
    }
)

app.register_blueprint(swaggerui_blueprint)
