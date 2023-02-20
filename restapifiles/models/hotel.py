
from database.sql_alchemy import banco


# Classe modelo para os hoteis:
class HotelModel(banco.Model): # herdando o Model do banco (SQL Alchemy)

    # Isto é uma tabela do banco de dados
    __tablename__ = 'hoteis' # Nome da tabela (SQL Alchemy)
    
    hotel_id = banco.Column(banco.String, primary_key = True)
    nome = banco.Column(banco.String(80)) # String com 80 caracteres
    estrelas = banco.Column(banco.Float(precision=1))
    diaria = banco.Column(banco.Float(precision=2))
    cidade = banco.Column(banco.String(30))
    
    
    # 
    def __init__(self, hotel_id, nome, estrelas, diaria, cidade) -> None:
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade
        
    def json(self):
        return {
            'hotel_id':self.hotel_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade
            }
    
    @classmethod
    def find_hotel (cls, hotel_id):
        # query.filter_by já é uma função do SQLAlchemy
        hotel = cls.query.filter_by(hotel_id=hotel_id).first() # SELECT * FROM hoteis WHERE hotel_id = $hotel_id$ LIMIT 1
        
        if hotel: # Se existe algum hotel
            return hotel
        return None

    # Em SQL Alchemy, os dados são salvo porque substituem quando já existe no banco
    def save_hotel(self): 
        
        # O self entende que os valores são os os atributos recebidos da classe
        banco.session.add(self) 
        banco.session.commit()