#: Crie uma função que receba os três lado de um triângulo e informe qual o tipo de triângulo formado ou "não é triangulo", caso não seja possível formar um triângulo.

# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro; 
# Triângulo Equilátero: três lados iguais; 
# Triângulo Isósceles: quaisquer dois lados iguais; 
# Triângulo Escaleno: três lados diferentes.

def tipo_triangulo (lado1, lado2, lado3):
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        if lado1 == lado2 == lado3:
            return 'Triângulo Equilátero'
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return 'Triângulo Isósceles'
        else:
            return 'Triângulo Escaleno'
    else:
        return 'Não é triângulo'

print(tipo_triangulo(3, 3, 3))