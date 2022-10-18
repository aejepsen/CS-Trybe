# Álcool:
# - Até 20 litros, desconto de 3% por litro;
# - Acima de 20 litros, desconto de 5% por litro.
# Gasolina:
# - Até 20 litros, desconto de 4% por litro;
# - Acima de 20 litros, desconto de 6% por litro.

# Escreva uma função que receba o número de litros vendidos, o tipo de combustível

A = 1.9
B = 2.5

def desconto(litros, tipo)
  if tipo == 'A'
    if litros <= 20
      litros * A * 0.97
    else
      litros * A * 0.95
    end
  else
    if litros <= 20
      litros * B * 0.96
    else
      litros * B * 0.94
    end
  end
end

puts desconto(20, 'A')