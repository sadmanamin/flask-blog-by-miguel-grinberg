from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager 
import logging
from logging.handlers import SMTPHandler
from flask_mail import Mail
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
mail = Mail(app)
bootstrap = Bootstrap(app)



from app import routes, models
from app import app, db
from app.models import User, Post, followers

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post,'followers':followers}



print(app.debug)
