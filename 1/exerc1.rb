#Crie uma função que receba dois números e retorne o maior deles.

puts "Digite um número:"
n1 = gets.chomp().to_i
puts "Digite outro número:"
n2 = gets.chomp().to_i

def maior(n1,n2)
  if n1 > n2
    puts "n1: #{n1} é maior que #{n2}"
  else
    puts "n2: #{n2} é maior que #{n1}"
  end
end

maior(n1,n2)