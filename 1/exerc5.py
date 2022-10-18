 # Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Crie uma função que retorne dois valores em uma tupla contendo a quantidade de latas de tinta a serem compradas e o preço total a partir do tamanho de uma parede (em m²).

def calcula_latas (area):
    litros = area / 3
    latas = litros / 18
    preco = latas * 80
    tupla_qtde_preco = (latas, preco)
    return tupla_qtde_preco

print(calcula_latas(100))