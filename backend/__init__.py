from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from sqlalchemy.sql import text
from flask_cors import CORS
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.secret_key = "password"
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'You must be logged in to access this page.'
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    db.init_app(app)
    migrate.init_app(app, db)

    # Create tables
    with app.app_context():
        db.create_all()

    # Register blueprints
    from .routes.auth_routes import auth_bp
    from .routes.company_routes import company_bp
    from .routes.job_routes import job_bp
    from .routes.application_routes import app_bp
    from .routes.form_routes import form_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(company_bp, url_prefix='/companies')
    app.register_blueprint(job_bp, url_prefix='/jobs')
    app.register_blueprint(app_bp, url_prefix='/applications')
    app.register_blueprint(form_bp, url_prefix='/forms')

    print(app.url_map)
    print(check_password_hash("scrypt:32768:8:1$AHC3h5IfUUV8evUO$c541acbae3dff4b58656e908040520c7e74d68b72f3e846d096aa07213d7e30ca3551cbe8b7e7aa0f2c6293795e97414528490a472a6bedefd2d43e30730a380","freak123"))



    return app


	








