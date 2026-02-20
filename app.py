from flask import Flask
from config import Config
from models import db
from controllers.client_controller import client_bp
from controllers.contact_controller import contact_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Register controllers
    app.register_blueprint(client_bp, url_prefix='/clients')
    app.register_blueprint(contact_bp, url_prefix='/contacts')

    @app.route('/')
    def home():
        return "<h2>CRM App Running</h2><p>Go to /clients or /contacts</p>"

    return app


# Create app instance for Gunicorn
app = create_app()

# Initialize database
with app.app_context():
    db.create_all()
    print("Database initialized!")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
