from . import db
from datetime import datetime

# -------------------- User Table --------------------
class User(db.Model):
    __tablename__ = "users"

    # Primary key
    id = db.Column(db.Integer, primary_key=True)

    # Unique email for user login
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Hashed password
    password = db.Column(db.String(256), nullable=False)

    # Timestamp of account creation
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# -------------------- Chart Data Table --------------------
class ChartData(db.Model):
    __tablename__ = "chartdata"

    # Primary key
    id = db.Column(db.Integer, primary_key=True)

    # Label for the chart segment (e.g. 'Linux', 'United States')
    label = db.Column(db.String(100), nullable=False)

    # Numeric value associated with the label
    value = db.Column(db.Float, nullable=False)

    # Type of chart this data belongs to (e.g. 'device', 'location', 'growth')
    type = db.Column(db.String(50), nullable=False)
