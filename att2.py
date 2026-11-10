matriz = []
contador = 1

for i in range(10): 
    linha = []
    
    for j in range(10): 
        linha.append(contador)
        contador += 1

    matriz.append(linha)

for linha in matriz:
    for elemento in linha: 
        print(f"{elemento:3}", end=" ")
    print()
