from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os
from dotenv import load_dotenv
from sqlalchemy import text

# Load environment variables from .env file
load_dotenv()

# Initialize database and migration extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configure the database URI from environment variable
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize SQLAlchemy with the Flask app
    db.init_app(app)

    # Enable CORS for all routes under /api/*
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Set up Flask-Migrate for handling database migrations
    migrate.init_app(app, db)

    # Test the database connection on app startup
    try:
        with app.app_context():
            with db.engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print("Database connection successful")
    except Exception as e:
        print("Database connection failed")
        print("Error:", e)

    # Register the API blueprint
    from .routes import api
    app.register_blueprint(api)

    return app
