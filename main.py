from gestaopatio import app  
 # Crie o banco de dados dentro do contexto da aplicação
with app.app_context():
       #database.drop_all()
       database.create_all()
    
    
    
if __name__ == '__main__':
        handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
        handler.setLevel(logging.ERROR)
        app.logger.addHandler(handler)
        app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False, use_debugger=False)