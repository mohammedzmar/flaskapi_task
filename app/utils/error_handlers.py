from flask import Blueprint, jsonify
from app.utils.custom_exceptions import NotFoundError

error_bp = Blueprint("errors", __name__)

@error_bp.app_errorhandler(NotFoundError)
def handle_not_found(e):
    return jsonify({"status": "error", "message": str(e)}), 404

@error_bp.app_errorhandler(Exception)
def handle_generic(e):
    return jsonify({"status": "error", "message": "Internal server error"}), 500
