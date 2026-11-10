matriz = []
soma = 0
for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input("Digite o n "))
        linha.append(valor)
        soma += valor[i],[j]
    matriz.append(linha)
    
for linha in matriz:
    print(linha)

print(soma)   