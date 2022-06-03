# Saudando
"""
def Saudacao(saudacao, nome):
    print(f'{saudacao}{nome}')

Saudacao('Olá ', 'João')
Saudacao('Olá ', 'jose')
Saudacao('Olá ', 'pedro')
"""
# Crie uma função que recebe 3 numeros como paramentros e exiba a soma entre eles:
"""OK
def Soma(numero1, numero2, numero3):
    soma = float(numero1) + float(numero2) + float(numero3)
    return soma
total = Soma(1,2,3)

print ('A soma entre estes 3 numeros é: ', total)

"""
# crie uma função que receba 2 numeros, o primeiro é uma valor e o segundo um percentual (ex 10%.) retorne o valor do primeiro número somado do aumento do percentual do mesmo.
"""
def SomaPercentual(valor, percentual):
    print (valor + (valor * percentual / 100))

SomaPercentual(1,100)
"""

# Fizz Buz - se o parametro da função for divisivel por 3, retorne Fizz, se o parâmetro da função for divisiel por 5, retorne Buzz. 
# Se o parametro da funçãofor divisivel por 5 e por 3 retorne FizBzz caso contrario retorne numero enviado:
def FizzBuzz(numero):
    int(numero)
    divide3 = numero % 3
    divide5 = numero % 5
    if divide3 == 0 and divide5 == 0:
        print('Numero ', numero, ' divisível por 3 e 5. FizzBuzz')
    if divide3 == 0 and divide5 != 0:
        print('Numero ', numero, ' divisível apenas por 3. Fizz')
    if divide5 == 0 and divide3 != 0:
        print('Numero', numero, ' divisível apenas por 5. Buzz')
    if divide3 != 0 and divide5 != 0:
        print('O numero', numero, 'não é divisível por 3 ou 5')

entrada = input('qual o valor, meu chapa? ')
FizzBuzz(entrada)




