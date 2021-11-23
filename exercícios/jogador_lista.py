dados = dict()
gols = list()
todos = list()


while True:
    dados["nome"] = input("Nome do jogador: ")

    partidas = int(input(f"Quantas partidas {dados['nome']} jogou? "))
    for p in range(0, partidas):
        gols.append(int(input(f"Quantos gols na partida {p}: ")))

    dados["gols"] = gols[:]
    gols.clear()
    dados["total"] = sum(dados["gols"])

    todos.append(dados.copy())
    dados.clear()

    continuar = " "
    while continuar not in "SN":
        continuar = input("Quer continuar? [S/N] ")[0].upper()
    if continuar == "N":
        break


print("-" * 60)

print(f"{'Cod':<5}{'Nome':<15}{'Gols':<15}{'Total':<5}")

print("-" * 40)

for k, v in enumerate(todos):
    print(f"{k:<5}{v['nome']:<15}{str(v['gols']):<15}{v['total']:<5}") 

print("-" * 40)

while True:
    menu = int(input("Mostrar dados de qual jogador? (999 interrompe) "))

    if menu < len(todos):
        print(f"Levantamento do jogador {todos[menu]['nome']}:")
        for k, v in enumerate(todos[menu]['gols']):
            print(f"  No jogo {k + 1} fez {v} gols")

    if menu == 999:
        break










# for k, v in dados.items():
#     print(f"O campo {k} tem o valor {v}")

# print("-" * 60)

# print(f"O jogador {dados['nome']} jogou {len(dados['gols'])} partidas.")
# for k, v in enumerate(dados["gols"]):
#     print(f" -> Na partida {k}, fez {v} gols.")

