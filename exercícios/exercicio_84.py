"""
Exercício de Python número 84 do canal Curso em Vídeo do professor Gustavo Guanabara
Faça um programa que leia nome e peso de várias pessoas, guardanto tudo em uma lista.
No final, mostre:
a) Quantas pessoas foram cadastradas
b) Uma listagem com as pessoas mais pesadas
c) Uma listagem com as pessoas mais leves

"""

cont = maior = menor = 0
pessoas = []
pessoa = []

while True:
    pessoa.append(input('Nome: '))
    pessoa.append(float(input('Peso: ')))
    if cont == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    cont += 1
    pessoas.append(pessoa[:])
    pessoa.clear()   
    
    parada = ' '
    while parada not in 'SN':
        parada = input('Quer continuar? [S/N] ').upper().strip()[0]
    if parada == 'N':
        break


print(f'Ao todo, você cadastrou {cont} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')

print(f'\nO menor peso foi de {menor}Kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
