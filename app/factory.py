from flask import Flask
import os
from .celery_utils import init_celery
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()
migrate = Migrate()


PKG_NAME = os.path.dirname(os.path.realpath(__file__)).split("/")[-1]

def create_app(app_name=PKG_NAME, **kwargs):
    app = Flask(app_name)
    app.config.from_object(config)

    if kwargs.get("celery"):
        init_celery(kwargs.get("celery"), app)


    db.init_app(app)
    migrate.init_app(app, db)

    from app import models
    from app.all import bp
    app.register_blueprint(bp)
    return app
