from dataclasses import dataclass


@dataclass
class Jogador:
    nome: str
    pontuacao: int
    lvl: float

time = []

for i in range(3):
    print(f"\n Cadastro do jogador {i+1}")
    nick = input("Digite o nome do jogador: ")
    pont = int(input("Digite a pontuação do jogador: "))
    lv = float(input("Digite o lvl do jogador: "))

novoJogador = Jogador(nome=nick, pontuacao=pont, lvl=lv)
time.append(novoJogador)

melhor_jogador = time[0]
for jg in time:
    if jg.pontuacao > melhor_jogador.pontuacao:
        melhor_jogador = jg

print(f"MVP do Time: {melhor_jogador.nickname}")
print(f"Pontuação: {melhor_jogador.pontuacao}")

