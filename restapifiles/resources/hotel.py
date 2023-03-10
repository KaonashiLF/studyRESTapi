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
        
        #List comprehension to get all hotels in json format
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}
    
    
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
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot be left blank")
    atributos.add_argument('estrelas', type=float)
    atributos.add_argument('diaria', type=float)
    atributos.add_argument('cidade', type=str, required=True, help="The field 'cidade' cannot be left blank")
    
    
    
    # -----------------------------------------------------------------
    # ---------------------------- Funções ----------------------------
    # -----------------------------------------------------------------

    # Get function to get hotel information searching for hotel_id
    # -----------------------------------------------------------------
    # The paremeter hotel_id have to be equal to the implementation 
    def get(self, hotel_id): 
        
        # Loop passing through to the list 
        hotel = HotelModel.find_hotel(hotel_id=hotel_id)
        
        if hotel: # Se existe hotel, retorna hotel
            return hotel.json() # retorna json() que é a transformação dos dados para json
        
        # Se não existe o hotel, ele irá sair do if acima e vai retornar essa mensagem
        return {'message': 'Hotel not found'}, 404 # Status code of not found
    
    

    # POST function to insert a new value in JSON file
    # -----------------------------------------------------------------
    
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"message":"Hotel id '{}' already exists".format(hotel_id)}, 400 # Bad request status code
        # Istância do método construtor, onde obtém os dados para passar
        
        dados = Hotel.atributos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'An internal error ocurred trying to save hotel'}, 500 # Interal Error
        return hotel.json()



# PUT function will update values if exists, but if doesn't exist, PUT function will create new hotel

    def put(self, hotel_id):
        dados = Hotel.atributos.parse_args()
        hotel_encontrado = HotelModel.find_hotel(hotel_id)
        
        # Se o hotel é encontrado, então atualiza com dados recebidos e salva
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200
        
        # Se não é encontrado, novo hotel é salvo usando o save_hotel
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message':'An internal error ocurred trying to save hotel'}, 500
        return hotel.json(), 201 # Created
        
    
    def delete(self, hotel_id):
        global hoteis
        
        # List comprehension
        
        # variável hoteis 
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        
        hotel = HotelModel.find_hotel(hotel_id)
        
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return{'message': 'An internal error ocurred trying to delete this hotel'}, 500
            return {"message": "Hotel '{}' deleted.".format(hotel_id)}, 200
        
        return {'message': 'Hotel not found.'}, 404