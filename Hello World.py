from flask import Flask #importa biblioteca flask

app = Flask(__name__) # Objeto app da classe flask

@app.route("/") #operator que define a rota
def hello_world(): #função a ser executada na rota "/"
    return "<p>Hello, World!</p>"

app.run(debug = True, port = 80) #inicia o servidor na porta 80 (tag debug=true para auxiliar no log de erros)
