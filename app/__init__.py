from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os
from dotenv import load_dotenv
from sqlalchemy import text

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # ✅ Properly indented CORS setup
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    migrate.init_app(app, db)

    try:
        with app.app_context():
            with db.engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print("✅ Database connection successful ✅")
    except Exception as e:
        print("❌ Database connection failed ❌")
        print("Error:", e)

    from .routes import api
    app.register_blueprint(api)

    return app
