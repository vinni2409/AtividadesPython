matriz = []
c_por_linha = [] 

for i in range(6):
    linha = []
    qtd_nesta_linha = 0  
    
    for j in range(8):
        valor = int(input(f"Digite o valor de [{i}] e [{j}]: "))
        linha.append(valor)
        
        if valor < 0:
            qtd_nesta_linha += 1  
            
    matriz.append(linha)
    c_por_linha.append(qtd_nesta_linha)  

print("\nMatriz final:")
for linha in matriz:
    print(linha)

print("\nQuantidade de números negativos por linha:")

for indice, quantidade in enumerate(c_por_linha):
    print(f"Linha {indice}: tem {quantidade} número(s) negativo(s)")