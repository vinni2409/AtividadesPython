ordem = 7
MI = []

for i in range(ordem):
    linha = []
    for j in range(ordem):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    MI.append(linha)

for linha in MI:
    for elemento in linha:
        print(elemento, end=" ")
    print()
