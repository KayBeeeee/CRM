# app.py
import os
from flask import Flask
from config import Config
from models import db
from controllers.client_controller import client_bp
from controllers.contact_controller import contact_bp

def create_app():
    app = Flask(__name__)

    # Load config
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(client_bp, url_prefix="/clients")
    app.register_blueprint(contact_bp, url_prefix="/contacts")

    # Home route
    @app.route("/")
    def home():
        return "<h2>CRM App Running</h2><p>Go to /clients or /contacts</p>"

    # Create tables automatically
    with app.app_context():
        db.create_all()
        print("Database initialized!")

    return app


# For local development
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=8080)
