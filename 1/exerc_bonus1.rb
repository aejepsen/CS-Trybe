# Dada uma lista, descubra o menor elemento. Por exemplo, 
lista = [5, 9, 3, 19, 70, 8, 100, 2, 35, 27]

# def menor_elemento(lista)
#   menor = lista[0]
#   lista.each do |elemento|
#     if elemento < menor
#       menor = elemento
#     end
#   end
#   return menor
# end

# def menor_elemento(lista)
#   menor = lista[0]
#   lista.each { |elemento| menor = elemento if elemento < menor }
#   return menor
# end

def menor_elemento(lista)
  lista.min
end

puts menor_elemento(lista)