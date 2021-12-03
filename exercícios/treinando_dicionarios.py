from datetime import datetime


dados = dict()

dados["nome"] = input("Nome:")
nascimento = int(input("Ano de nascimento: "))
dados["idade"] = datetime.today().year - nascimento
dados["ctps"] = int(input("Carteira de trabalho: (0 não tem): "))
if dados["ctps"] != 0:
    ano_contratacao = int(input("Ano de contratação: "))
    dados["contratação"] = datetime.today().year - ano_contratacao
    dados["salário"] = float(input("Salário: R$ "))
    dados["aposentadoria"] = (ano_contratacao - nascimento) + 35


print('-' * 50)
for k, v in dados.items():
    print(f"- {k} tem o valor {v}")
