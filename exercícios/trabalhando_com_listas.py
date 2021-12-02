completa = []
pares = []
impares = []


while True:
    num = int(input("Digite um número: "))

    if num % 2 == 0:
        completa.append(num)
        pares.append(num)
    else:
        completa.append(num)
        impares.append(num)

    cont = " "
    while cont not in "SsNn":
        cont = input("Quer continuar? [S/N] ")[0].upper().strip()
    if cont in "Nn":
        break


print(f"A lista completa é: {completa}")
print(f"A lista de pares é: {pares}")
print(f"A lista de ímpares é: {impares}")



# lista = []

# while True:
#     lista.append(int(input("Digite um valor: ")))

#     cont = " "
#     while cont not in "SsNn":
#         cont = input("Quer continuar? [S/N] ")[0].upper().strip()
#     if cont in "Nn":
#         break


# print(f"Você digitou {len(lista)} elementos.")

# lista.sort(reverse = True)
# print(f"Os valores em ordem decrescentes são: {lista}")

# if 5 in lista:
#     print("O valor 5 faz parte da lista")
# else:
#     print("O valor 5 não faz parte da lista")

