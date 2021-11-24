from random import randint
from time import sleep

todos = []
temp = []

jogos = int(input("Quantos jogos você quer que eu sorteie? "))

while True:
    while True:
        num = randint(1, 61)
        if num not in temp:
            temp.append(num)
        if len(temp) == 6:
            break
    todos.append(temp[:])
    temp.clear()
    if len(todos) == jogos:
        break



for j in todos:
    print(j)
    sleep(0.5)

