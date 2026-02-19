from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from models.client import Client
        from models.contact import Contact
        db.create_all()

    from controllers.client_controller import client_bp
    from controllers.contact_controller import contact_bp

    app.register_blueprint(client_bp)
    app.register_blueprint(contact_bp)

    @app.route("/")
    def index():
        return "CRM App Running"

    return app
