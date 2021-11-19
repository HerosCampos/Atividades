nums = (
    int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: '))
)

print(f'Você digitou os valores: {nums}')

if 3 in nums:
    print(f'O valor 3 está na {nums.index(3) + 1}ª posição.')
else:
    print('O valor 3 não está na lista.')

print(f'O valor 9 apareceu {nums.count(9)} vezes.')

print(f'Os valores pares digitados foram:', end = ' ')
cont = 0
for n in nums:
    if n % 2 == 0:
        print(n)
        cont += 1

print(f'No total foram {cont} números pares.')


