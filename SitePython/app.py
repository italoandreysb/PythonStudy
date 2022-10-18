from flask import Flask, render_template
# A função??? "render_template" já buscas as páginas html dentro de template

app = Flask(__name__)

# route -> hashtreinamentos.com/
# função -> o que você quer exibir naquela página.
# template ->

#criando o route padrão para home 
@app.route("/")
def homepage():
    return render_template("homepage.html")

# Criando o route para a página de contatos
@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

# Criando página com o nome de qualquer usuário
@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# Criando o route para a página de login
@app.route("/login")
def login():
    return render_template("login.html")

# Colocar o site no ar, o debug já tenta colocar as coisas no ar
if __name__ == "__main__":
    app.run(debug=True)  # "debug=True" permite que qualquer atualização seja feita

# Será hospedado no servidor do Heroku