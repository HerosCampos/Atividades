from random import randrange
from time import sleep

jogo = list()
todos_jogos = list()

quantidade = int(input('Quantos jogos você quer? '))


for n in range(0, quantidade):
    while(True):
        num = randrange(1, 60)
        
        if num not in jogo:
            jogo.append(num)
        
        if len(jogo) == 6:
            break
    
    todos_jogos.append(jogo.copy())
    jogo.clear()


for k, v in enumerate(todos_jogos):
    print(f'Jogo {k + 1}: {sorted(v)}')
    sleep(0.5)
