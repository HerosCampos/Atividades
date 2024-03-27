maior = menor = 0

for p in range(1, 8, 1):
    peso_pessoa = float(input(f"Peso da {p}ª pessoa: "))

    if p == 1:
        maior = peso_pessoa
        menor = peso_pessoa
    else:
        if peso_pessoa > maior:
            maior = peso_pessoa
        elif peso_pessoa < menor:
            menor = peso_pessoa


print(f"O maior peso lido foi de {maior}")
print(f"O menor peso lido foi de {menor}")

