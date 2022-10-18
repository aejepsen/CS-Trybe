#: Crie uma função que receba os três lado de um triângulo e informe qual o tipo de triângulo formado ou "não é triangulo", caso não seja possível formar um triângulo.

# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro; 
# Triângulo Equilátero: três lados iguais; 
# Triângulo Isósceles: quaisquer dois lados iguais; 
# Triângulo Escaleno: três lados diferentes.

def tipo_triangulo(lado1, lado2, lado3)
  if lado1 + lado2 > lado3 && lado1 + lado3 > lado2 && lado2 + lado3 > lado1
    if lado1 == lado2 && lado1 == lado3
      return "Triângulo Equilátero"
    elsif lado1 == lado2 || lado1 == lado3 || lado2 == lado3
      return "Triângulo Isósceles"
    else
      return "Triângulo Escaleno"
    end
  else
    return "Não é triângulo"
  end
end

puts tipo_triangulo(2, 2.1, 1)