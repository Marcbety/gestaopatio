from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from dotenv import load_dotenv
import os

# Inicializa a aplicação Flask
app = Flask(__name__)

# Configurações principais

load_dotenv()

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['WTF_CSRF_ENABLED'] = True

# Inicializa extensões
database = SQLAlchemy(app)
migrate = Migrate(app, database)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

# Função para carregar o usuário logado
@login_manager.user_loader
def load_usuario(id_usuario):
  from gestaopatio.models import Usuario
  return Usuario.query.get(int(id_usuario))

# Importa as rotas da aplicação
from gestaopatio import routes
