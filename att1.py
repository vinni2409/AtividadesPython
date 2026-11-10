# Criando uma matriz vazia 7x9

matriz = []

soma = 0

# Leitura da matriz

for i in range(7):

  linha = []

  for j in range(9):

    valor = int(input(f"Digite o elemento da linha {i} e coluna {j}: "))

    linha.append(valor)

    soma = soma + valor

  matriz.append(linha)

# Mostrando a matriz

print("\nMatriz digitada:")

for i in range(7):

  print(matriz[i])

print(f"\nA soma de todos os elementos é: {soma}")
