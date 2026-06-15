import os

from flask import Flask
from dotenv import load_dotenv

from app.config import config_by_name, DevelopmentConfig

load_dotenv()


def create_app():
    app = Flask(__name__)

    config_name = os.getenv("FLASK_CONFIG", "development")
    config_obj = config_by_name.get(config_name, DevelopmentConfig)

    app.config.from_object(config_obj)

    from app.api.auth import auth_bp
    from app.api.metrics import metrics_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(metrics_bp)

    @app.route("/")
    def home():
        return {"success": True, "message": "Metrics Running"}

    return app
