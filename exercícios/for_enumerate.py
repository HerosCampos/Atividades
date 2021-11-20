lista = []
maior = menor = 0

for n in range(0, 5):
    lista.append(int(input(f"Digite um valor para a posição {n}: ")))

print(f'Você digitou os valores {lista}.')
print(f'O maior valor é {max(lista)}. Nas posições', end = " ")
for k, v in enumerate(lista):
    if v == max(lista):
        print(k, end = " ")

print(f'\nO menor valor é {min(lista)}. Nas posições', end = " ")
for k, v in enumerate(lista):
    if v == min(lista):
        print(k, end = " ")
