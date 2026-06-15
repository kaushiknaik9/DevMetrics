from flask import Flask
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)

    from app.api.auth import auth_bp
    from app.api.metrics import metrics_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(metrics_bp)

    @app.route("/")
    def home():
        return {"success": True, "message": "Metrics Running"}

    return app
