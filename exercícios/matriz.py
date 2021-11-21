matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_terceira = maior_valor = 0

for i in range(0, 3):
    for c in range(0, 3):
        matriz[i][c] = int(input(f"Digite um valor para [{i}, {c}]: "))
        if matriz[i][c] % 2 == 0:
            soma_par += matriz[i][c]
        if matriz[i][2]:
            soma_terceira += matriz[i][2]
        if matriz[1][c]:
            maior_valor = matriz[1][c]
        else:
            if matriz[1][c] > maior_valor:
                maior_valor = matriz[1][c]
        


for i in range(0, 3):
    for c in range(0, 3):
        print(f"[ {matriz[i][c]} ]", end = " ")
    print()


print(f"A soma dos valores pares é: {soma_par}")
print(f"A soma dos valores da terceira coluna é: {soma_terceira}")
print(f"O maior valor da segunda linha é {maior_valor}")
    