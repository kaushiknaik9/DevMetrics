from flask import request, Blueprint

auth_bp = Blueprint("auth", __name__, url_prefix="/api/v1/auth")

auth_bp.route("/register", methods=["POST"])


def register():
    data = request.get_json()
    return {"success": True, "message": "Register endpoint working", "data": data}, 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    return {"success": True, "message": "Login endpoint working", "data": data}, 200
