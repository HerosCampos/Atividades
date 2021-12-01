principal = [[], []]


for n in range(0, 7):
    num = int(input(f"Digite o {n + 1}º valor: "))

    if num % 2 == 0:
        principal[0].append(num)
    else:
        principal[1].append(num)


print(f'Os valores pares digitados foram: {principal[0]}')
print(f"Os valores ímpares digitados foram: {principal[1]}")
