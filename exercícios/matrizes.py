"""
Exercícios 86 e 87 do canal Curso em Vídeo do professor Gustavo Guanabara.
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.

Aprimore o desafio mostrando:
a) A soma de todos os valores pares digitados
b) A soma dos valores da terceira coluna
c) O maior valor da segunda linha
"""
pares = tercCol = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


for col in range(0, 3):
    for lin in range(0, 3):
        matriz[col][lin] = int(input(f'Insira um valor para a posição [{col}, {lin}]: '))
        if matriz[col][lin] % 2 == 0:
            pares += matriz[col][lin]


print('-' * 80)

for col in range(0,3):
    for lin in range(0, 3):
        print(f'[{matriz[col][lin]:^5}]',end='')
    print()

print('-' * 80)

print(f'A soma dos valores pares é {pares}.')
for lin in range(0, 3):
    tercCol += matriz[lin][2]

print(f'A soma dos valores da terceira coluna é {tercCol}.')

print(f'O maior valor da segunda linha é {max(matriz[1])}')

# Outra possibilidade 
maior = 0
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]


print(f'O maior valor da segunda linha é {maior}.')

