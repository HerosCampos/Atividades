matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somaCol = 0


for i in range(3):
    for n in range(3):
        matriz[i][n] = int(input(f"Digite um valor para [{i}, {n}]: "))
        if matriz[i][n] % 2 == 0:
            soma += matriz[i][n]



print(matriz)

for l in range(3):
    for k in range(3):
        print(f'[ {matriz[l][k]} ]', end = ' ')
    print()


print('-----------------')
print(f'A soma dos valores pares é: {soma}')

for i in range(3):
    somaCol += matriz[i][2]

print(f'A soma dos valores da terceira coluna é: {somaCol}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')















