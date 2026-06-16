from flask import Blueprint, jsonify

users_bp = Blueprint("users", __name__, url_prefix="/api/v1/users")

users = []


@users_bp.route("/users")
def get_users():
    return {"success": True, "message": "All the Users are listed Below", "data": users}
