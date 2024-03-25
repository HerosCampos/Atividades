nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

print(f"Tirando {nota1} e {nota2}, a media do aluno e: {media}")

if media < 5:
    print('O aluno esta reprovado.')
elif media >= 5 and media < 6:
    print('O aluno esta em recuperacao')
else:
    print('O aluno esta aprovado')

