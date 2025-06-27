import logging
from logging.handlers import RotatingFileHandler
from gestaopatio import app, database

# Cria o banco de dados dentro do contexto da aplicação
with app.app_context():
    # database.drop_all()  # Use com cuidado!
    database.create_all()

if __name__ == '__main__':
    # Configura o log de erros
    handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.ERROR)
    app.logger.addHandler(handler)

    # Inicia o servidor Flask
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
