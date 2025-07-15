from flask import Blueprint, request, jsonify, make_response
from flask_cors import cross_origin
from . import db
from .models import User, ChartData
from .auth import hash_password, check_password
from sqlalchemy import func
from datetime import datetime, timedelta
import jwt
import os

# Load secret key for JWT from environment variable or fallback default
SECRET_KEY = os.environ.get("SECRET_KEY", "fef7c0b0106ae4c4cab8bdf911db754ea8119c7e14a67836e9ac4199d3836eb9")

# Create a blueprint for all API routes
api = Blueprint("api", __name__, url_prefix="/api")

# -------------------- USER REGISTRATION --------------------
@api.route("/signup", methods=["POST"])
@cross_origin()
def signup():
    # Ensure the request is JSON
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    # Validate required fields
    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    # Check for duplicate user
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 400

    # Create and save the new user
    user = User(email=email, password=hash_password(password))
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# -------------------- USER LOGIN --------------------
@api.route("/signin", methods=["POST"])
@cross_origin()
def login():
    # Ensure the request is JSON
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    # Validate required fields
    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    # Fetch user from database
    user = User.query.filter_by(email=email).first()

    # Verify credentials and generate token
    if user and check_password(password, user.password):
        token = jwt.encode(
            {"user_id": user.id, "exp": datetime.utcnow() + timedelta(days=1)},
            SECRET_KEY,
            algorithm="HS256"
        )
        return jsonify({
            "message": "Login successful",
            "access_token": token,
            "user_id": user.id
        }), 200

    return jsonify({"error": "Invalid email or password"}), 401

# -------------------- DASHBOARD STATS --------------------
@api.route("/dashboard-stats", methods=["GET"])
@cross_origin()
def dashboard_stats():
    # Returns mock summary stats for dashboard cards
    return jsonify({
        "Views": "721K",
        "Visits": "450K",
        "New Users": "1,167",
        "Active Users": "453K"
    })

# -------------------- USER GROWTH CHART DATA --------------------
@api.route("/user-growth", methods=["GET"])
@cross_origin()
def user_growth():
    # Fetch user growth chart data
    data = ChartData.query.filter_by(type="growth").all()
    return jsonify({
        "labels": [d.label for d in data],
        "values": [d.value for d in data]
    })

# -------------------- DEVICE TRAFFIC CHART DATA --------------------
@api.route("/traffic-by-device", methods=["GET"])
@cross_origin()
def traffic_by_device():
    # Fetch traffic data categorized by device
    data = ChartData.query.filter_by(type="device").all()
    return jsonify({
        "labels": [d.label for d in data],
        "values": [d.value for d in data]
    })

# -------------------- LOCATION TRAFFIC CHART DATA --------------------
@api.route("/traffic-by-location", methods=["GET"])
@cross_origin()
def traffic_by_location():
    # Fetch traffic data categorized by location
    data = ChartData.query.filter_by(type="location").all()
    return jsonify({
        "labels": [d.label for d in data],
        "values": [d.value for d in data]
    })
