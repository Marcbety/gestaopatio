
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configurações principais
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'chave-padrao-secreta')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///data/agendamento.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['WTF_CSRF_ENABLED'] = True

# Inicializa extensões
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

# Carregamento do usuário
@login_manager.user_loader
def loade_usuario(id_usuario):
  from gestaopatio.models import Usuario
  return Usuario.query.get(int(id_usuario))

# Importa rotas
from gestaopatio import routes
