from flask import Flask
from .home import home


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(home)