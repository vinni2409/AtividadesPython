from dataclasses import dataclass


@dataclass
class Livro:
    titulo: str
    autor: str
    anoPublicacao: int


biblioteca = []

for i in range(2):
    print(f"\nCadastro do Livro {i+1}")
    tit = input("Digite o nome do livro: ")
    aut = input("Digite o nome do autor: ")
    anoPub = int(input("Digite o ano da publicação: "))

    novoLivro = Livro(titulo=tit, autor=aut, anoPublicacao=anoPub)
    biblioteca.append(novoLivro)

livroVelho = biblioteca[0]

for lv in biblioteca:
    if lv.anoPublicacao < livroVelho.anoPublicacao:
        livroVelho = lv

print(f"\nLivro mais velho: {livroVelho.titulo} ({livroVelho.anoPublicacao}) - Autor: {livroVelho.autor}")
