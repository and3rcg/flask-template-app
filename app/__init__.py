import os

from flask import Flask
from flask_cors import CORS

from app.api.routes import api
from app.exception_handlers import register_exception_handlers
from app.frontend.routes import frontend

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'db.sqlite3')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
    #     or 'sqlite:///' + DB_PATH
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # initializing blueprints
    app.register_blueprint(frontend)
    app.register_blueprint(api)

    # misc setup: cors and exception handlers
    CORS(app)
    register_exception_handlers(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8000, load_dotenv=True)

