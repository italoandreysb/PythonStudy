# Função que sauda:
# Geralmente não se utilizar print dentro de função, e sim o return
# uma função pode retornar qualquer coisa em pyhton
#==Exemplo 01
"""
def saudacao(mensagem='Olá', nome='Bípede'):  # Os campos nome e olá tem valores para caso sejam vazios, preencher.
    nome = nome.replace('e', '3')
    mensagem = mensagem.replace('e', '3')
    return f'{mensagem} {nome}'
saudacao('Valor que eu quero')  # Estou mandando o texto para a função

# entrada = input('Pode falar:')
# resultado = saudacao()  #chamando a função

print (resultado)
"""
# ---------------
# Função divisão:
#----------------

def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2

divide = divisao(5,5)

if divide:
    print(divide)
else:
    print('Conta inválida.')

""" Verificando id/local da memória da função divisao

print (id(divisao))
"""