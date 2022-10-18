# Álcool:
# - Até 20 litros, desconto de 3% por litro;
# - Acima de 20 litros, desconto de 5% por litro.
# Gasolina:
# - Até 20 litros, desconto de 4% por litro;
# - Acima de 20 litros, desconto de 6% por litro.

# Escreva uma função que receba o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A - álcool, G - gasolina), e retorne o valor a ser pago pelo cliente, sabendo-se que o preço do litro da gasolina é R$ 2,50, e o preço do litro do álcool é R$ 1,90

A = 1.9
G = 2.5 
def valor_a_pagar(litros, tipo):
    if tipo == "A":
        if litros <= 20:
            return litros * A * 0.97
        else:
            return litros * A * 0.95
    else:
        if litros <= 20:
            return litros * G * 0.96
        else:
            return litros * G * 0.94

print(valor_a_pagar(11, "G"))