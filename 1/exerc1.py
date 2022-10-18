#Crie uma função que receba dois números e retorne o maior deles.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

def maior(n1, n2):
    if n1 > n2:
        return print(f'{n1} é maior que {n2}')
    else:
        return print(f'{n2} é maior que {n1}')

maior(n1,n2)