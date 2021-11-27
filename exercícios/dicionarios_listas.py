dados = dict()
lista = list()
soma_idade = 0

while True:
    dados["nome"] = input("Nome: ")

    dados["sexo"] = " "
    while dados["sexo"] not in "MF":
        dados["sexo"] = input("Sexo: [M/F] ")[0].upper()

    dados["idade"] = int(input("Idade: "))
    soma_idade += dados["idade"]

    lista.append(dados.copy())
    dados.clear()

    continuar = " "
    while continuar not in "SN":
        continuar = input("Quer continuar? [S/N] ")[0].upper()
    if continuar == "N":
        break
    


print(f"Ao todo temos {len(lista)} cadastradas.")

print(f"A média de idade é {soma_idade / len(lista)}")

print(f"As mulheres cadastradas foram:", end = " ")
for p in lista:
    if p["sexo"] in "Ff":
        print(f"{p['nome']}", end = " ")

print(f"\nLista das pessoas que estão acima da média:")
for p in lista:
    if p["idade"] > soma_idade / len(lista):
        print()
        for k, v in p.items():
            print(f"  {k} = {v}")

    