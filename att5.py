linhas = 15
colunas = 20
matriz = []
soma_colunas = [0] * colunas 

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = float(input(f"Digite o valor para a posição da linha {i}, coluna {j}: "))
        linha.append(valor)
        soma_colunas[j] += valor
        
    matriz.append(linha)

print("\nMatriz 15x20: ")
for linha in matriz:
    print(linha)

print("\nSoma Separada por Coluna: ")
for j in range(colunas):
    print(f"Soma da Coluna {j}: {soma_colunas[j]}")