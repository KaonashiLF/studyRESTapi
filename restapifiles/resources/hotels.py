# Este arquivo terá todos os recursos que são relacionados com hoteis

from flask_restful import Resource, reqparse


hoteis = [
    
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'São Paulo'
    },
    {
        'hotel_id': 'bravo',
        'nome': 'Bravo Hotel',
        'estrelas': 4.4,
        'diaria': 380.99,
        'cidade': 'Rio de Janeiro'
    },
    {
        'hotel_id': 'charlie',
        'nome': 'Charlie Hotel',
        'estrelas': 3.9,
        'diaria': 290.05,
        'cidade': 'Santa Catarina'
    },
    {
        'hotel_id': 'ibis_guara',
        'nome': 'Ibis Guaratinguetá Hotel',
        'estrelas': 3.5,
        'diaria': 140.26,
        'cidade': 'Guaratinguetá'
    },
    {
        'hotel_id': 'ibis_lorena',
        'nome': 'Ibis Lorena Hotel',
        'estrelas': 3.2,
        'diaria': 120.26,
        'cidade': 'Lorena'
    } 
]

class Hoteis (Resource):
    '''
    This is a class of hotels
    Inheriting Resources from library flask_resful
    '''
    def get(self):
        hotels = hoteis
        return hotels
    
    
class Hotel (Resource):
    
    def find_hotel(hotel_id):
        for hotel in hoteis: 
            # If this id exists, then it will return hotel (above)
            if hotel['hotel_id'] == hotel_id: 
                return hotel
        return None
    
    # Get function to get hotel information searching for hotel_id
    # -----------------------------------------------------------------
    # The paremeter hotel_id have to be equal to the implementation 
    def get(self, hotel_id): 
        
        # Loop passing through to the list 
        hotel = Hotel.find_hotel(hotel_id=hotel_id)
        
        if hotel: # Se existe hotel, retorna hotel
            return hotel
        
        # Se não existe o hotel, ele irá sair do if acima e vai retornar essa mensagem
        return {'message': 'Hotel not found'}, 404 # Status code of not found
    
    
    
    # POST function to insert a new value in JSON file
    # -----------------------------------------------------------------
    
    def post(self, hotel_id):
        
        hotel = Hotel.find_hotel(hotel_id=hotel_id)
        
        # Se existe hotel, então ele irá retornar esta mensagem, senão continuará seguindo o código
        if hotel is not None:
            error_message = f'The hotel_id {hotel_id} is already created!'
            return error_message,500
        
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome')
        argumentos.add_argument('estrelas')
        argumentos.add_argument('diaria')
        argumentos.add_argument('cidade')
        
        # Variável dados é o construtor
        
        # Ele recebe os valores passados no .add_argument acima, pois pertencem a mesma classe
        
        
        dados = argumentos.parse_args()
        
        new_hotel = {
            'hotel_id': hotel_id,
            'nome': dados['nome'],
            'estrelas': dados['estrelas'],
            'diaria': dados['diaria'],
            'cidade': dados['cidade']
        }
        
        hoteis.append(new_hotel)
        
        return new_hotel, 200


# PUT function will update values if exists, but if doesn't exist, PUT function will create new hotel

    def put(self, hotel_id):
        pass
    
    def delete(self, hotel_id):
        pass