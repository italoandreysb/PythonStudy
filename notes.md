## Anotações curso de API

### Preparando o ambiente:

1. Instale o Python:

```
apt install python3
```

2. Ajuste o apelido:
```
alias python=python3.8.10
```
3. Instalando o virtualenv com o PIP:
```
apt install pip
pip install virtualenv
```
4. Criar o ambiente virtual:
`
```
virtualenv ambvir --python=python3
```

5. Ativando ambiente:

```
source ambvir/bin/activate
```

6. Desabilitando o ambiente:

```
deactivate
```

7. Instalando bibliotecas (dentro do ambvir):

```
pip install Flask
pip install Flask-Restful
```

8. Verificar bibliotecas instaladas:

```
pip freeze 
```

### Criando arquivo requirements:

1. Instale as bibliotecas, ex:

```
pip install Flask
pip install Flask-Restful
```

2. Liste as bibliotecas:

```
Pip freeze
```

3. Copie a saída e cole num arquivo chamado "requirements.txt"

4. Instale as bibliotecas a partir do arquivo com o comando:

```Pip install -r requirements.txt```