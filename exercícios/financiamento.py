valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salario da pessoa que quer comprar a casa? '))
quantos_anos = int(input('O pagamento sera feito em quantos anos? '))

quantidade_prestacoes = 12 * float(quantos_anos)

mensalidade = valor_casa / quantidade_prestacoes
print(mensalidade, salario * 0.3)
if mensalidade < salario * 0.30:
    print('Emprestimo aprovado, a mensalidade representa menos que 30% do salario da pessoa.')
else:
    print('Emprestimo reprovado, a mensalidade representa mais que 30% do salario da pessoa.')
