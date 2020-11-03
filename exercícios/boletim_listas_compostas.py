"""
Exercício 89 da lista de Python do canal Curso em Vídeo do professor Gustavo Guanabara.
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
de cada aluno individualmente.
"""

dados = []
lista = []

while True:
    nome = input('Nome: ')
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    dados.append(nome)
    dados.append(nota_1)
    dados.append(nota_2)
    dados.append(media)
    lista.append(dados[:])
    dados.clear()

    parada = ' '
    while parada not in 'SN':
        parada = input('Quer continuar? [S/N] ').upper().strip()[0]
    if parada == 'N':
        break


print('-' * 40)
print(f"{'Nº':<5}{'Nome':<25}{'Média':<10}")
print('-' * 40)

for p, v in enumerate(lista):
    print(f"{p:<5}{v[0]:<25}{v[3]:<10}")
print('-' * 40)

while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 para parar) '))
    if mostrar < len(lista):
        print(f'As notas do aluno {lista[mostrar][0]} foram: {lista[mostrar][1]} e {lista[mostrar][2]}.')
    elif mostrar == 999:
        break
