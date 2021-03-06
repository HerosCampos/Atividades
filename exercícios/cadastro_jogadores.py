"""
Exercícios 93 e 95 do curso de Python do canal Curso em Vídeo do professor Gustavo Guanabara.
Crie um programa que gerencie o aproveitamente de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso 
será guardado em um dicionário, incluindo o total de gols feitos durante o campeonado.

Aprimore o exercício 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização 
de detalhes do aproveitamento de cada jogador.
"""


dados = dict()
gols = list()
todos = list()

while True:
    dados['nome'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

    for j in range(0, partidas):
        gols.append(int(input(f'  - Quantos gols na partida {j}: ')))
        
    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    gols.clear()
    todos.append(dados.copy())
    dados.clear()
    
    while True:
        parada = input('Quer continuar? [S/N] ').upper().strip()[0]
        if parada in "SN":
            break
        print('Opção inválida, tente novamente...')
    if parada == 'N':
        break


print('-=' * 40)
print(f"{'Cod':<5}{'Nome':<15}{'Gols':<15}{'Total':<5}")
print('-' * 40)
for k, v in enumerate(todos):
    print(f'{k:<5}{v["nome"]:<15}{str(v["gols"]):<15}{v["total"]:<5}')
print('-' * 40)

while True:
    mostrar = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if mostrar == 999:
        break
    elif mostrar < len(todos):
        print(f'Mostrar levantamento do jogador {todos[mostrar]["nome"]}.')
        for k, v in enumerate(todos[mostrar]["gols"]):
            print(f"  No jogo {k + 1} fez {v} gols.")