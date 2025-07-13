from flask import Blueprint, request, jsonify, make_response
from . import db
from .models import User
from .auth import hash_password, check_password
from sqlalchemy import func

api = Blueprint("api", __name__, url_prefix="/api")

# -------------------- SIGNUP --------------------
@api.route("/signup", methods=["POST", "OPTIONS"])
def signup():
    if request.method == "OPTIONS":
        return handle_options_response()

    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 400

    user = User(email=email, password=hash_password(password))
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


# -------------------- LOGIN --------------------
@api.route("/login", methods=["POST", "OPTIONS"])
def login():
    if request.method == "OPTIONS":
        return handle_options_response()

    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()

    if user and check_password(password, user.password):
        return jsonify({
            "message": "Login successful",
            "user_id": user.id
        }), 200

    return jsonify({"error": "Invalid email or password"}), 401


# -------------------- DASHBOARD DATA --------------------
@api.route("/dashboard-data", methods=["GET"])
def dashboard_data():
    user_count = User.query.count()
    dummy_visits = 1200
    dummy_signups = user_count
    dummy_sales = 150

    return jsonify({
        "stats": {
            "visits": dummy_visits,
            "signups": dummy_signups,
            "sales": dummy_sales,
        },
        "chart": {
            "labels": ["Jan", "Feb", "Mar"],
            "values": [10, 30, 50]
        }
    })


# -------------------- GET USER BY ID --------------------
@api.route("/user/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify({
        "id": user.id,
        "email": user.email,
        "created_at": user.created_at
    })


# -------------------- Handle Preflight --------------------
def handle_options_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    return response, 200
