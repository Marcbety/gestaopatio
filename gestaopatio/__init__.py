from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
    
    
app.config['SECRET_KEY'] = 'ed9af17758e577d8e0aaa8f22a87b6bbf4ead56536'
if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI']=os.getenv("DATABASE_URL")
else:    
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///agendamento.db'
app.config['WTF_CSRF_ENABLED'] = True
    
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from gestapatio import routes
