# app.py
import os
from flask import Flask
from config import Config
from models import db
from controllers.client_controller import client_bp
from controllers.contact_controller import contact_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    database_url = os.environ.get("DATABASE_URL")

    if database_url:
        # Force SQLAlchemy to use pymysql instead of MySQLdb
        if database_url.startswith("mysql://"):
            database_url = database_url.replace(
                "mysql://",
                "mysql+pymysql://",
                1
            )

        app.config["SQLALCHEMY_DATABASE_URI"] = database_url

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(client_bp, url_prefix="/clients")
    app.register_blueprint(contact_bp, url_prefix="/contacts")

    @app.route("/")
    def home():
        return "<h2>CRM App Running</h2><p>Go to /clients or /contacts</p>"

    with app.app_context():
        db.create_all()
        print("Database initialized!")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
