listagem = (
    'lapis', 1.75,
    'Borracha', 2.00,
    'Caderno', 15.90,
    'Estojo', 36.00,
    'Transferidor', 4.99,
    'Compasso', 9.99,
    'Mochila', 120.99,
    'Canetas', 22.49,
    'Livros', 34.90
)

print(f'-' * 40)
print(f'{"Listagem de preços":^40}')
print(f'-' * 40)


for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f"{listagem[i]:.<30}R$", end = '')
    else:
        print(f"{listagem[i]:>8}")

