from flask import Flask
from flask_restful import Resource, Api

app = Flask (__name__)
api = Api(app)

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

api.add_resource(Hoteis, '/hoteis')

if __name__ == '__main__':
    app.run(debug=True)