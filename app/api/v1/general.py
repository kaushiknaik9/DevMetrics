from flask import Blueprint, jsonify, current_app

general_bp = Blueprint("general", __name__, url_prefix="/v1/api/general")


@general_bp.route("/ping")
def ping():
    debug_mode = current_app.config["DEBUG"]
    return jsonify({"status": True, "message": "ping", "debug": debug_mode})


@general_bp.route("/hello")
def hello():
    return jsonify({"success": True, "message": "Hello Ping-Pong !!"})
