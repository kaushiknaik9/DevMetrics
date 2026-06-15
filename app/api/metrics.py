from flask import Blueprint, request

metrics_bp = Blueprint("metrics", __name__, url_prefix="/api/v1/metrics")

metrics = []


@metrics_bp.route("/", methods=["POST"])
def create_metric():
    data = request.get_json()

    metrics.append(data)

    return {"success": True, "message": "Metrics Created", "data": data}, 201


@metrics_bp.route("/", methods=["GET"])
def get_metric():
    return {"success": True, "count": len(metrics), "data": metrics}, 200


@metrics_bp.route("/<int:index>", methods=["DELETE"])
def delete_metrics(index):
    if index >= len(metrics):
        return {"success": False, "message": "Metrics not Found"}, 404

    deleted = metrics.pop(index)

    return {"success": True, "message": "Metric Deleted", "data": deleted}, 200
