 # Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Crie uma função que retorne dois valores em uma tupla contendo a quantidade de latas de tinta a serem compradas e o preço total a partir do tamanho de uma parede (em m²).

def calcula_latas(tamanho)

  litros = tamanho / 3.0
  latas = (litros / 18.0).ceil(2)
  preco = latas * 80
  tupla = [latas, preco]
  return tupla
end

puts calcula_latas(100)