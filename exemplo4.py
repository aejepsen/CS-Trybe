listas = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]

def maior_name(listas):
	maior = 0
	for lista in listas:
		if len(lista) > maior:
			maior = len(lista)
			nome = lista
	return nome
			
print(maior_name(listas))
