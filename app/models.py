from . import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ChartData(db.Model):
    __tablename__ = "chartdata"

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(100), nullable=False)   # e.g., "Linux", "Mac", "USA"
    value = db.Column(db.Float, nullable=False)          # e.g., 20000000
    type = db.Column(db.String(50), nullable=False)      # e.g., "device", "location", "growth"

