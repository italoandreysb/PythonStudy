import sqlite3

connection = sqlite3.connect('banco.db')  # Criar banco
cursor = connection.cursor()  # O cursor seleciona o conteúdo no banco de dados

# Criação de tabela
cria_tabela = "CREATE TABLE IF NOT EXISTS hoteis \
    (hotel_id text PRIMARY KEY, nome text, estrelas real, diaria real, cidade text)"

cria_hotel = "INSERT INTO hoteis VALUES ('Alpha', 'Alpha Hotel', 4.4, 250.50, 'Aracaju')"

cursor.execute(cria_tabela)
cursor.execute(cria_hotel)

connection.commit()  # Salvando o banco
connection.close()  # fechando a conexão

"""
Este script é independente, roda sem o código da API
"""