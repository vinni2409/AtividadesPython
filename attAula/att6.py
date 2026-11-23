while True:
  clienteBruto = input("Digite o nome do cliente (ou fim para acabar o processo): ")

  nomeSemEspaco = clienteBruto.strip()
  if not nomeSemEspaco:
    continue

  nomeFormatado = nomeSemEspaco.title()

  primeiroNome = nomeFormatado.split()[0]

  mensagem = f"Olá, {primeiroNome}! Seja bem vindo."
  print(mensagem)
  print("-" * 35)

  if "fim" in clienteBruto.lower():
    print("Programa encerrado. ")
    break
