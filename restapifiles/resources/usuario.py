# Este arquivo terá todos os recursos que são relacionados com hoteis

from flask_restful import Resource, reqparse
from models.usuario import UserModel



class Users (Resource):
    '''
    This is a class of hotels
    Inheriting Resources from library flask_resful
    '''
    def get(self):
        
        #List comprehension to get all hotels in json format
        return {'usuario': [user.json() for user in UserModel.query.all()]}
    
    
class User (Resource):
    '''
    Status Code Meaning\n
    200 -> Success\n
    201 -> Created\n
    404 -> Not Found\n
    500 -> Server Error
    '''
    # -----------------------------------------------------------------
    # ---------------- Atributos da minha classe Hotel ----------------
    # -----------------------------------------------------------------
    atributos = reqparse.RequestParser()
    atributos.add_argument('login', type=str, required=True, help="The field 'login' cannot be left blank")
    atributos.add_argument('senha', type=str, required=True, help="The field 'senha' cannot be left blank")
    
    
    
    # -----------------------------------------------------------------
    # ---------------------------- Funções ----------------------------
    # -----------------------------------------------------------------

    # Get function to get hotel information searching for hotel_id
    # -----------------------------------------------------------------
    # The paremeter hotel_id have to be equal to the implementation 
    def get(self, user_id): 
        
        # Loop passing through to the list 
        user = UserModel.find_user(user_id=user_id)
        
        if user: # Se existe user, retorna user
            return user.json() # retorna json() que é a transformação dos dados para json
        
        # Se não existe o user, ele irá sair do if acima e vai retornar essa mensagem
        return {'message': 'User not found'}, 404 # Status code of not found
    
    
        
    
    def delete(self, user_id):
        global usuarios
        
        # List comprehension
        # variável usuarios 
        usuarios = [user for user in usuarios if user['user_id'] != user_id]
        
        user = UserModel.find_user(user_id)
        
        if user:
            try:
                user.delete_user()
            except:
                return{'message': 'An internal error ocurred trying to delete this user'}, 500
            return {"message": "User '{}' deleted.".format(user_id)}, 200
        
        return {'message': 'User not found.'}, 404
    
    
class UserRegister(Resource):
    
    def post(self):
        atributos = reqparse.RequestParser()
        atributos.add_argument('login')
        atributos.add_argument('senha')