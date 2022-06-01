# Aplicação Rest com Crud em memória

## Crud funcional + classe modelo

- Método Get Post, Put e Delete OK e usando nova estrutura de classe modelo de hoteis e a conversão json
- Método de classe adicionado
- Método de conversão para Json adicionado
- pacote models criado e inserido os métodos acima

Passo a passo:

1. instale o Sql alchemy no ambvir
	# pip install Flask-SQLAlchemy

2. Crie o arquivo sql_alchemy.py e insira:

```Python
from flask_sql_alchemy import SQLAlchemy

banco = SQLAlchemy()

```
3. no arquivo app.py, abaixo do dunder main (__main__) adicione os campos comentados:

Obs: É adicionado no dunder main pois queremos que seja executado apenas do app.py.

```Python
from flask import Flask
from flask_restful import Api 
from resources.hotel import Hoteis, Hotel 

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
api = Api(app)

@app.before_first_request
def cria_banco():  
    banco.create_all()  #


api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')


if __name__ == '__main__': 
    from sql_alchemy import banco  #
    banco.init_app(app)    #
    app.run(debug=True) # 

```

Acesse o arquivo hotel.py e adicione as linhas comentadas:

```python

from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from sql_alchemy import banco # esta

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
        dados = Hotel.argumentos.parse_args() 
        hotel_objeto = HotelModel(hotel_id, **dados)   no "hotel_id"
        novo_hotel = hotel_objeto.json()   
        hoteis.append(novo_hotel) 
        return novo_hotel, 201

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()  
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)  
            return novo_hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, hotel_id):
        global hoteis 
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message': 'Hotel deleted.'}


    """
    - Sempre que "precisarmos" copiar e colar um códio para outro campo, pensar em criar uma classe
    

    """
```
 