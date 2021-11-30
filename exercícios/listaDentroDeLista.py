contador = maior = menor = 0
temp = []
principal = []

while True:
    temp.append(input("Nome: "))
    temp.append(float(input("Peso: ")))

    if contador == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:])
    temp.clear()
    contador += 1

    cont = " "
    while cont not in "SN":
        cont = input("Quer continuar? [S/N] ")[0].upper().strip()
    if cont == "N":
        break


print(f"Ao todo você cadastrou {contador} pessoas.")

print(f"O maior peso foi {maior}. Peso de:", end = " ")
for p in principal:
    if p[1] == maior:
        print(f"{p[0]}", end = " ")

print(f"\nO menor peso foi {menor}. Peso de:", end = " ")
for p in principal:
    if p[1] == menor:
        print(f"{p[0]}", end = " ")
