

from flask import Flask
from flask_cors import CORS
from Backend.routers.user import login
from Backend.routers.category_router import category
from Backend.routers.task_route import task
from flask_jwt_extended import JWTManager
from datetime import timedelta


def create_app():
    app = Flask(__name__)
    CORS(app)
    def add_header(response):
        response.headers['Cross-Origin-Opener-Policy'] = 'same-origin-allow-popups'
        return response
    app.register_blueprint(login)   
    app.register_blueprint(category)
    app.register_blueprint(task)
     
    app.config['JWT_SECRET_KEY'] = "_\xb9\x19Fp\x98\x9a\xb0\x0c\xce\x15_\xc6\x14\x00?cxA\xe8\x1b\xacn\xd1" 
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=5)
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=7)
    jwt = JWTManager(app)   
    return app



app = create_app() 
