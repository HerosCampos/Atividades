"""
Exercício 88 do curso de Python do canal Curso em Vídeo do professor Gustavo Guanabara
Faça um programa que ajude um jogador da MEGASENA a criar palpites. O promgrama vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando 
tudo em uma lista composta.
"""
from random import randrange
jogo = []
jogos = []
cont = 0
opc = int(input('Quantos jogos você quer sortear? '))
while cont < opc:
    while len(jogo) < 6:
        rand = randrange(61)
        if rand not in jogo:
            jogo.append(rand)
    print(jogo)
    jogos.append(jogo[:])
    jogo.clear()
    cont += 1
