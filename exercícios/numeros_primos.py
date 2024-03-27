
num = int(input("Digite um numero: "))
contador = 0

for i in range(1, num + 1, 1):
    if num % i == 0:
        print(i, end = ' ')
        contador += 1

print()
print(f"O numero {num} foi divisivel {contador} vezes")
if contador == 2:
    print('Por isso ele e um numero primo.')
else:
    print('Por isso ele nao e um numero primo.')
