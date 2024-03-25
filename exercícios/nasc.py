from datetime import date


while True:
    ano_nasc = int(input('Ano de nascimento: '))
    if ano_nasc >= 1000:
        break
    else:
        print('O ano deve conter 4 digitos')


ano_atual = date.today().year

print(f"Quem nasceu em {ano_nasc} tem {ano_atual - ano_nasc} em {ano_atual}")
if ano_atual - ano_nasc < 18:
    print(f"E ainda faltam {18 - (ano_atual - ano_nasc)} anos para o alistamento.")
    print(f"Seu alistamento sera em {ano_atual + (ano_atual - ano_nasc)}")
elif ano_atual - ano_nasc == 18:
    print('Parabens, voce esta na idade de alistar.')
else:
    print(f"Voce deveria ter se alistado em {ano_atual - ((ano_atual - ano_nasc) - 18)}")
