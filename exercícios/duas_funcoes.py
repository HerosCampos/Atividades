from random import randint


def sorteio():
    print(f"Sorteando 5 valores da lista:", end = " ")

    lista = list()
    
    for i in range(0, 5):
        num = randint(1, 10)
        lista.append(num)
        print(f"{num}", end = " ")
    return lista


def somaPar(lista):
    soma = 0
    for p in lista:
        if p % 2 == 0:
            soma += p
    print(f"\nSomando os valores pares de {lista}, temos {soma}.")


s = sorteio()
somaPar(s)

