
print('-' * 30)
print(f'{"LOJA SUPER BARATÃO":^30}')
print('-' * 30)
soma = mais_de_1000 = barato = cont = 0
barato_nome = ""

while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço: '))

    soma += preco

    if preco > 1000:
        mais_de_1000 += 1
    
    if cont == 0:
        barato = preco
        barato_nome = nome
    else:
        if preco < barato:
            barato = preco
            barato_nome = nome


    cont = " "
    while cont not in "SsNn":
        cont = input('Quer continuar? [S/N] ')
    if cont in "Nn":
        break


print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {mais_de_1000} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato_nome} que custa R$ {barato:.2f}')
