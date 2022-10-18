# Calcule a média aritmética dos valores contidos em uma lista.
lista = [1, 2, 3, 4, 5]
def media(lista):
    soma = 0
    for i in lista:
        soma += i
    return print(soma / len(lista))
media(lista)