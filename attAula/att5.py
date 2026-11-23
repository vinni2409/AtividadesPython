clienteBruto = "mARcos aUGuSto sIlva"

nomeLimpo = clienteBruto.strip()
nomeFormatado = nomeLimpo.title()
primeiroNome = nomeFormatado.split()[0]

print(f"Olá, {primeiroNome}! Seja bem-vindo.")
