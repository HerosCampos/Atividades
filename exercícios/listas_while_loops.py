lista = []


while True:
    val = int(input("Digite um valor: "))
    if val not in lista:
        lista.append(val)
    else:
        print("Valor duplicado, não será adicionado!")

    cont = " "
    while cont not in "SsNn":
        cont = input("Quer continuar? [S/N] ")
    if cont in "Nn":
        break

print(f'Você digitou os valores {lista}.')