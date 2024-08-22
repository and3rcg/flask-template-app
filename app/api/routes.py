from flask import Blueprint, jsonify

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/")
def index():
    return jsonify({"message": "Hello from backend!"}), 200

@api.route("/exception-test")
def test_exception():
    raise ValueError("it's ok, this is just a test")
