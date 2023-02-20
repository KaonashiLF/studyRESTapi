
from database.sql_alchemy import banco


# Classe modelo para os usuarios:
class UserModel(banco.Model): # herdando o Model do banco (SQL Alchemy)

    # Isto é uma tabela do banco de dados
    __tablename__ = 'usuarios' # Nome da tabela (SQL Alchemy)
    
    user_id = banco.Column(banco.Interger, primary_key = True)
    login = banco.Column(banco.String(40)) # String com 40 caracteres
    senha = banco.Column(banco.String(40))
    
    # 
    def __init__(self, user_id, login, senha) -> None:
        self.login = login
        self.senha = senha

        
    def json(self):
        return {
            'user_id':self.user_id,
            'login': self.login,
            }
    
    @classmethod
    def find_user (cls, user_id):
        # query.filter_by já é uma função do SQLAlchemy
        user = cls.query.filter_by(user_id=user_id).first() # SELECT * FROM usuarios WHERE user_id = $user_id$ LIMIT 1
        
        if user: # Se existe algum user
            return user
        return None

    # Em SQL Alchemy, os dados são salvo porque substituem quando já existe no banco
    def save_user(self): 
        
        # O self entende que os valores são os os atributos recebidos da classe
        banco.session.add(self) 
        banco.session.commit()
        
    def update_user(self, nome, estrelas, diaria, cidade):
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade
        
    def delete_user(self):
        banco.session.delete(self)
        banco.session.commit()