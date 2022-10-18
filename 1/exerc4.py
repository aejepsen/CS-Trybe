# Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de caracteres. Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"], o retorno deve ser "Fernanda"

lista = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]
def maior_nome(lista):
    maior = 0
    for i in lista:
        if len(i) > maior:
            maior = len(i)
            nome = i
    return print(nome)

maior_nome(lista)