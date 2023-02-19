# Este arquivo terá todos os recursos que são relacionados com hoteis

from flask_restful import Resource, reqparse
from models.hotel import HotelModel




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
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
    
    
    
    # -----------------------------------------------------------------
    # ---------------------------- Funções ----------------------------
    # -----------------------------------------------------------------

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
        if HotelModel.find_hotel(hotel_id=hotel_id):
            return {'message':'Hotel id "{}" already exists'.format(hotel_id)}, 400 # Bad request status code
        # Istância do método construtor, onde obtém os dados para passar
        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        
        hotel.save_hotel()
        
        return hotel.json()
        # new_hotel = hotel.json()
        
        
        # hoteis.append(new_hotel)
        
        # return new_hotel, 200



# PUT function will update values if exists, but if doesn't exist, PUT function will create new hotel

    def put(self, hotel_id):
        
        hotel = Hotel.find_hotel(hotel_id=hotel_id)
        
        dados = Hotel.argumentos.parse_args()
        
        # **dados é um kwargs que recebe key e args, ou seja, dicionario. Quando utilizo **dados, estou desempacotando a variável dados.
        # Na variável dados eu tenho todos os argumentos que preciso para registrar um novo hotel
        hotel_objeto = HotelModel(hotel_id, **dados) 
        
        new_hotel = hotel_objeto.json() 
        
        if hotel: # Se o hotel já existe, então atualiza
            hotel.update(new_hotel)
            # message = 'Hotel atualizado com sucesso!'
            return new_hotel, 200 # Atualiza o hotel
        
        # Se não existe, cria o hotel
        hoteis.append(new_hotel)
        # message = 'Hotel adicionado com sucesso'
        return new_hotel, 201 # Created status
    
    def delete(self, hotel_id):
        global hoteis
        
        # List comprehension
        
        # variável hoteis 
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        
        return {'message': 'Hotel deleted.'}, 200       