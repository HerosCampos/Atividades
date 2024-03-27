
cont = soma = maior = menor = 0

while True:
    num = int(input("Digite um numero: "))

    if cont == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    cont += 1
    soma += num

    continuar = input('Quer continuar? [S/N] ').strip()
    while continuar not in "SsNn":
        continuar = input("Opcao errada, quer continuar? [S/N] ")
    if continuar in "Nn":
        break


print(f"Voce digitou {cont} numeros e a media foi de {soma / cont}")
print(f"O maior valor foi {maior} e o menor valor foi {menor}")

