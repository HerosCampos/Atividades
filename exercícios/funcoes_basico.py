def umDez():
    print("Contagem de 1 até 10 de 1 em 1")
    for i in range(0, 10):
        print(i + 1, end = " ")
    print("Fim!")
    print('-' * 50)


def DezZero():
    print("Contagem de 10 até 0 de 2 em 2")
    for i in range(10, -1, -2):
        print(i, end = " ")
    print("Fim!")
    print('-' * 50)


def personalizado1():
    print("Contagem personalizada 1")
    inicio = int(input("Início: "))
    fim = int(input("Fim: "))
    passo = int(input("Passo: "))

    for i in range(inicio, fim, passo):
        print(i, end = " ")
    print("Fim!")


def personalizado2(inicio, fim, passo):
    print("Contagem personalizada 2")
    for i in range(inicio, fim, passo):
        print(i, end = " ")
    print("Fim!")


umDez()
DezZero()
personalizado1()
personalizado2(17, 1, -2)


# ---------------------------------------------------------------------

def analise_valores(*nums):
    print("Analisando valores passados...")
    for i in nums:
        print(i, end = " ")
    print(f"\nForam informados {len(nums)} ao todo.")
    print(f"O maior valor foi {max(nums)}.")
    print(f"O menor valor foi {min(nums)}.")
    

analise_valores(2, 3, 4, 6, 88)


# ---------------------------------------------------------------------


def fatorial(fat, show = False):
    if show == True:
        for n in range(fat, 0, -1):
            print(n, end = "")
            if n > 1:
                print(" x ", end = "")
            else:
                print(" = ", end = "")
    mult = 1
    for n in range(1, fat + 1, 1):
        mult *= n
    print(mult)


fatorial(5)


# ---------------------------------------------------------------------


def leiaInt(n):
    num = str(input(n))

    while True: 
        if num.isnumeric():
            num = int(num)
            return num
            break
        else:
            print("Erro! Digite um número inteiro válido...")
            num = str(input(n))



n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")


# ---------------------------------------------------------------------


def notas(*n, sit = True):
    analise_notas = dict()
    analise_notas['total'] = sum(n)
    analise_notas["maior"] = max(n)
    analise_notas["menor"] = min(n)
    analise_notas["média"] = sum(n) / len(n)
    if sit == True:
        if analise_notas["média"] >= 7:
            analise_notas["situação"] = "Aprovador"
        elif 5 <= analise_notas["média"] < 7:
            analise_notas["situação"] = "Recuperação"
        else:
            analise_notas["situação"] = "Reprovado"

    return analise_notas


resp = notas(5.5, 7.5, 9.5, sit = True)
print(resp)


