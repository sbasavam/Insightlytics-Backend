from flask import Blueprint, request, jsonify, make_response
from flask_cors import cross_origin
from . import db
from .models import User, ChartData
from .auth import hash_password, check_password
from sqlalchemy import func
from datetime import datetime, timedelta
import jwt
import os

SECRET_KEY = os.environ.get("SECRET_KEY", "fef7c0b0106ae4c4cab8bdf911db754ea8119c7e14a67836e9ac4199d3836eb9")

api = Blueprint("api", __name__, url_prefix="/api")

# -------------------- SIGNUP --------------------
@api.route("/signup", methods=["POST"])
@cross_origin()
def signup():
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
@api.route("/signin", methods=["POST"])
@cross_origin()
def login():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()

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


# -------------------- Other Routes Remain Same --------------------

@api.route("/dashboard-stats", methods=["GET"])
@cross_origin()
def dashboard_stats():

    return jsonify({
        "Views": "721K",
        "Visits": "450K",
        "New Users": "1,167",
        "Active Users": "453K"
    })

@api.route("/user-growth", methods=["GET"])
@cross_origin()
def user_growth():
    data = ChartData.query.filter_by(type="growth").all()
    return jsonify({
        "labels": [d.label for d in data],
        "values": [d.value for d in data]
    })

@api.route("/traffic-by-device", methods=["GET"])
@cross_origin()
def traffic_by_device():
    data = ChartData.query.filter_by(type="device").all()
    return jsonify({
        "labels": [d.label for d in data],
        "values": [d.value for d in data]
    })

@api.route("/traffic-by-location", methods=["GET"])
@cross_origin()
def traffic_by_location():
    data = ChartData.query.filter_by(type="location").all()
    return jsonify({
        "labels": [d.label for d in data],
        "values": [d.value for d in data]
    })
