lista = ('Lápis', 1.75,
        'Borracha', 2,
        'Caderno', 15.90,
        'Estojo', 25,
        'Transferidor', 4.2,
        'Compasso', 9.99,
        'Mochila', 120.32,
        'Canetas', 22.30,
        'Livro', 34.90)


for k, v in enumerate(lista):
    if k % 2 == 0:
        print(f'{v:.<30}', end = '')
    else:
        print(f'R${v:>10}')