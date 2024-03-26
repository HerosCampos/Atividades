# Exercicio 44 do professor Guanabara

preco = float(input("Qual o preco das compras: R$"))
user_prompt = int(input("""
FORMAS DE PAGAMENTO
[ 1 ] a vista no dinheiro
[ 2 ] a vista no cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao
[ 5 ] sair
Qual a sua opcao? """))

if user_prompt == 1:
    print(f"Sua compra de {preco} vai custar {preco * 0.9} a vista.")
elif user_prompt == 2:
    print(f"Sua compra de {preco} vai custar {preco * 0.95} no cartao.")
elif user_prompt == 3:
    print(f"Sua compra vai custar {preco} dividido em duas vezes.")
elif user_prompt == 4:
    print(f"Sua compra de {preco} vai custar {preco * 1.2} dividido duas ou mais vezes no cartao.")
else:
    print(f"Opcao errada, tente novamente.")

