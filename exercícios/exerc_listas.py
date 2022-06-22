lista = list()
maior = menor = 0


for i in range(0, 5):
    lista.append(int(input(f'Digite o número para a posição {i}: ')))


for k, n in enumerate(lista):
    if k == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n


print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end = ' ')
for k, n in enumerate(lista):
    if n == maior:
        print(k, end = ' ')

print()

print(f'O menor valor digitado foi {menor} nas posições ', end = ' ')
for k, n in enumerate(lista):
    if n == menor:
        print(k, end = ' ')