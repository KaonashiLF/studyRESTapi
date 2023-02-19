from flask import Flask
from flask_restful import Api
from resources.hotels import * # importing class Hoteis from resources/hotels.py


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # Configurando caminho do banco
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Retirar avisos de modificações
api = Api(app)

# O REST API criado será com base em um hotel

# Adding the path which will be used to consult in postman

# Método Decorador
@app.before_first_request # Ao executar este arquivo, ele verifica se existe um banco
def create_database():
    banco.create_all()

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')


# This code for run my app variable with debug function
if __name__ == '__main__':
    # Este import está sendo realizado dentro desta condição porque
    # só iremos importar o SQL Alchemy quando ocorrer a execução do arquivo app.py
    
    # Posteriormente este arquivo também será importado nos outros arquivos e para que ele não seja importado toda hora, coloca-se na condicional onde o app.py seja o importador principal, quando executado
   
    from database.sql_alchemy import banco
    banco.init_app(app) # 
    app.run(debug=True)
