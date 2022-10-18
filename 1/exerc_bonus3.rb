# Crie uma função que receba um número inteiro N e retorne o somatório de todos os números de 1 até N. Por exemplo, para N = 5, o valor esperado será 15 (1 + 2 + 3 + 4 + 5 = 15).

# def somatorio(n)
#   (1..n).reduce(:+)
# end

# def somatorio(n)
#   (1..n).reduce { |sum, i| sum + i }
# end

# def somatorio(n)
#   (1..n).inject(:+)
# end

# def somatorio(n)
#   (1..n).inject { |sum, i| sum + i }
# end

def somatorio(n)
  (1..n).sum
end

puts somatorio(6)