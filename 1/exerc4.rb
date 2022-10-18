# Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de caracteres. Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"], o retorno deve ser "Fernanda"

lista = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]

def maior_nome(lista)
  maior = lista[0]
  lista.each do |nome|
    if nome.length > maior.length
      maior = nome
    end
  end
  maior
end

puts maior_nome(lista)