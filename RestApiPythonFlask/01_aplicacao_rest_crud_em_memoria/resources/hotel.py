from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [
        {
        'hotel_id': 'alpha',
        'nome': 'Alpha hotel',
        'estrelas:': 4.3,
        'diaria': 400,
        'cidade': 'Rio de Janeiro'
        },
        {
        'hotel_id': 'bravo',
        'nome': 'Bravo hotel',
        'estrelas:': 4.3,
        'diaria': 400,
        'cidade': 'Rio de Janeiro'
        },
        {
        'hotel_id': 'charlie',
        'nome': 'Charlie hotel',
        'estrelas:': 4.3,
        'diaria': 400,
        'cidade': 'Rio de Janeiro'
        }
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}


class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    # Método para validação de função (verifica se há hotel existente)
    def find_hotel(hotel_id):  
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {'message': 'hotel not found'}, 404 

    def post(self, hotel_id):
        dados = Hotel.argumentos.parse_args()  # construtor
        hotel_objeto = HotelModel(hotel_id, **dados)  # Varável "hotel_objeto" recebe todos argumentos(**dados) da classe "hotel" baseado no "hotel_id"
        novo_hotel = hotel_objeto.json()  # variável "novo_hotel" recebe a conversão .json do "hotel_objeto" 
        hoteis.append(novo_hotel)  # função .append() usada para criar um novo hotel
        return novo_hotel, 201

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()  # o parse_args chama todo o construtor 
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)  # a função ".update()" já trabalha com os updates
            return novo_hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, hotel_id):
        global hoteis  # Tornando a variável "hoteis" global
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message': 'Hotel deleted.'}


    """
    - Sempre que "precisarmos" copiar e colar um códio para outro campo, pensar em criar uma classe
    

    """