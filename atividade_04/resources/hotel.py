from flask_restful import Resource

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
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'message': 'hotel not found'}, 404 #Status code http, not found

    def post(self, hotel_id):
        pass

    def put(self, hotel_id):
        pass
    
    def delete(self, hotel_id):
        pass