from flask import Flask
from app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    from app.extensions import db, login_manager
    db.init_app(app)
    login_manager.init_app(app)
    
    # Register blueprints
    from app.auth import bp as auth_bp
    from app.main import bp as main_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    
    return app