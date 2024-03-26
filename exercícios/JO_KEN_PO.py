from random import randrange


opt_list = ['Pedra', 'Papel', 'Tesoura']
opt = int(input("""
Sua opcoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual e a sua jogada? """))


print('=-=-=-=-=-=-=-=-=-=')

computador = randrange(0, 3)
print(f"O computador jogou {opt_list[computador]}")
print(f"Voce jogou {opt_list[opt]}")

print('=-=-=-=-=-=-=-=-=-=')

if computador == 0:
    if opt == 0:
        print("Deu empate!")
    elif opt == 1:
        print("Jogador vence!")
    elif opt == 2:
        print("Computador vence!")
elif computador == 1:
    if opt == 0:
        print('Computador vence!')
    elif opt == 1:
        print('Deu empate!')
    elif opt == 2:
        print('Jogador vence!')
elif computador == 2:
    if opt == 0:
        print('Jogador vence!')
    elif opt == 1:
        print('Computador vence!')
    elif opt == 2:
        print('Deu empate!')
