from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

login = LoginManager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login.login_view = 'login'
login.login_message = 'Please Login!'
login.login_message_category = 'info'

from app import routes, models