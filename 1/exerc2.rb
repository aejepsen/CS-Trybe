# Calcule a média aritmética dos valores contidos em uma lista.
lista = [1, 2, 3, 4, 5]

soma = 0
# lista.each do |valor|
#   soma += valor
# end

for valor in lista
  soma += valor
end

media = soma / lista.size.to_f
puts "A média é #{media}"
