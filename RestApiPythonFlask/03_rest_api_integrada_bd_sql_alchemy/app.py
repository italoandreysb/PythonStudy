from flask import Flask
from flask_restful import Api 
from resources.hotel import Hoteis, Hotel 

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db' # dizer como queremos a criação do banco, definindo o caminho e diretório do banco
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # cancela as mensagens de notificação
api = Api(app)

@app.before_first_request
def cria_banco():  # Metodo para criar todoas as tabelas do banco
    banco.create_all()  #


api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

#Toda aplicação python tem, significa que se o nome é padrão (app), a aplicação roda
if __name__ == '__main__': 
    from sql_alchemy import banco  #
    banco.init_app(app)    #
    app.run(debug=True) # 