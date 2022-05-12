from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



# initializing plug-ins
login = LoginManager()

# init my database
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class = Config):
    # init the app
    app = Flask(__name__)

    # link in the config
    app.config.from_object(config_class)

    # Register Plug-Ins
    login.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # Configure Some Settings
    login.login_view = 'auth.login'
    login.login_message = 'Please Login!'
    login.login_message_category = 'info'

    from .blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from .blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from .blueprints.build import bp as build_bp
    app.register_blueprint(build_bp)

    return app
