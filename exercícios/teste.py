from random import randrange

cont = 0

num_pc = randrange(1, 11)

print(f"O computador escolheu um num entre 0 e 10, tente adivinhar...")

palpite = int(input("Qual o seu palpite? "))

while palpite != num_pc:
    if palpite > num_pc:
        print(f"Menos... Tente mais uma vez.")
    else:
        print(f"Mais... Tente mais uma vez.")

    cont += 1    
    palpite = int(input("Qual o seu palpite? "))

print(f"Voce acertou com {cont} tentativas.")
