from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:111@localhost:5432/belajarflask'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Import and register routes
    from app.routes.coffeeRoutes import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
