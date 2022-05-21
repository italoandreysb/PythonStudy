from flask import Flask
from flask_restful import Api # Essa lib já converte para json
from resources.hotel import Hoteis, Hotel #Importando o pacote

app = Flask (__name__)
api = Api(app)

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

#Toda aplicação python tem, significa que se o nome é padrão (app), a aplicação roda
if __name__ == '__main__': 
    app.run(debug=True) # Debug true é apenas para teste
