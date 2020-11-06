from random import randrange
from time import sleep

def sorteia(lista):
    print('Os números sorteados foram: ', end='')
    for cont in range(0, 5):
        n = randrange(10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.5)
    print()
    

def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lista}: temos {soma}')


nums = list()
sorteia(nums)
somaPar(nums)
