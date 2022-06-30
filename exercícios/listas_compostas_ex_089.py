pessoa = list()
todos = list()


while(True):
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))

    pessoa.append(nome)
    pessoa.append(nota1)
    pessoa.append(nota2)
    pessoa.append((nota1 + nota2) / 2)

    todos.append(pessoa.copy())
    pessoa.clear()

    parar = input("Quer continuar? [S/N] ").strip().upper()[0]
    while parar not in "SN":
        parar = input("Opção errada! Quer continuar? [S/N] ").strip().upper()[0]
    if parar == 'N':
        break


print('-' * 27)
print(f"{'No':<5}{'NOME':<15}{'MÉDIA':<7}")
print('-' * 27)
for k, v in enumerate(todos):
    print(f" {k:<5}{v[0]:<15}{v[3]:<7}")


while(True):
    aluno = int(input("Mostrar notas de qual aluno? (999 para parar) "))

    if aluno < len(todos):
        print(f"O aluno escolhido foi {todos[aluno][0]} e as notas foram: {todos[aluno][1]} e {todos[aluno][2]}.")

    if aluno == 999:
        break

