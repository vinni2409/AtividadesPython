import random 

linhas = 20
colunas = 15

matriz = [[random.randint(1, 10) for _ in range(colunas)] for _ in range(linhas)]

soma_linhas_pares = 0

for i in range(linhas): 
    if i % 2 == 0:
        soma_linhas_pares += sum(matriz[i])

print(matriz)
print(f"A soma dos elementos das linhas pares é: {soma_linhas_pares}")