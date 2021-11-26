temp = list()
lista = list()
soma = 0

while True:
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    soma = nota1 + nota2
    
    temp.append(nome)
    temp.append(nota1)
    temp.append(nota2)
    temp.append(soma / 2)

    lista.append(temp[:])
    temp.clear()

    continuar = " "
    while continuar not in "SN":
        continuar = input("Quer continuar? [S/N] ")[0].upper().strip()
    if continuar == "N":
        break


print('-' * 60)
print(f"{'Nº':<5}{'Nome':<30}{'Média':<10}")
print('-' * 60)

for k, v in enumerate(lista):
    print(f"{k:<5}{v[0]:<30}{v[3]:<10}")


while True:
    notas = int(input("Mostrar notas de qual aluno? (999 interrompe) "))

    if notas < len(lista):
        print(f"As notas de {lista[notas][0]} são: {lista[notas][1]} e {lista[notas][2]}.")

    if notas == 999:
        break

