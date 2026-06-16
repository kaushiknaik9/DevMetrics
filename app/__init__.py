import os
from flask import Flask
from app.config import config_map, DevelopmentConfig
from app.extensions import db, migrate


def create_app(config_name=None):

    app = Flask(__name__)

    if config_name is None:
        config_name = os.environ.get("FLASK_ENV", "development")

    selected_config_name = config_map.get(config_name, DevelopmentConfig)

    app.config.from_object(selected_config_name)

    db.init_app(app)
    migrate.init_app(app, db)
    # this connects db to app
    # one initiates db and the connects db to app

    from app.models import tenant, user, metric, report

    from app.api.v1.general import general_bp
    from app.api.v1.users import users_bp

    app.register_blueprint(general_bp)
    app.register_blueprint(users_bp)

    return app
