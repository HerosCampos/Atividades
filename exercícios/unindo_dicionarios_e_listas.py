"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista. No final, mostra:
a) Quantas pessoas cadastradas
b) A média de idade
c) Uma lista com mulheres
d) Uma lista com idade acima da média
"""

dados = dict()
todos = list()
cont = soma = 0

while True:
    dados['nome'] = input('Nome: ')
    while True:
        dados['sexo'] = input('Sexo: [M/F] ').upper().strip()[0]
        if dados['sexo'] in 'MF':
            break
        print('Opção inválida, digite M para masculino e F para Feminino.')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    todos.append(dados.copy())
    dados.clear()
    cont += 1


    while True:
        parada = input('Quer continuar? [S/N] ').upper().strip()[0]
        if parada in 'SN':
            break
        print('Opção inválida, tente novamente...')
    if parada == 'N':
        break
    print('-' * 60)


print(todos)
print(f'Ao todo temos {cont} pessoas cadastradas.')
print(f'A média de idade é de {(soma / cont):.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for p in todos:
    if p['sexo'] == 'F':
        print(f'[{p["nome"]}]', end=' ')

print('\nLista de pessoas que estão com idade acima da média:')
for p in todos:
    if p['idade'] >= (soma / cont):
        print(f'  - Nome: {p["nome"]}; Sexo: {p["sexo"]}; Idade: {p["idade"]}')