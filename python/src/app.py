from flask import Flask
from src.config import config
from src.controllers import register_blueprints
from src.extensions import register_extensions
from dotenv import load_dotenv
load_dotenv()

def create_app():
    """Minimal App for simple flask app."""
    app = Flask(__name__)
    app.config.from_object(config)
    
    register_extensions(app)
    register_blueprints(app)
    return app


def create_worker_app():
    """Minimal App without routes for celery worker."""
    app = Flask(__name__)
    app.config.from_object(config)
    
    register_extensions(app, worker=True)
        
    return app
