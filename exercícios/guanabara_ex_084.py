lista = list()
cont = maior = menor = 0

while(True):
    nome = input('Nome: ')
    lista.append(nome)
    peso = float(input("Peso (Kg): "))
    lista.append(peso)

    if cont == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

    cont += 1

    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    while(continuar not in "SN"):
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break


print(f'\nAo todo, você cadastrou {cont} pessoas.')

print(f'O maior peso foi de {maior}Kg. Peso de:', end = ' ')
for n in range(len(lista)):
    if lista[n] == maior:
        print(lista[n - 1], end = ' ')

print()

print(f'O menor peso foi de {menor}Kg. Peso de:', end = ' ')
for n in range(len(lista)):
    if lista[n] == menor:
        print(lista[n - 1], end = ' ')

