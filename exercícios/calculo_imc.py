peso = float(input('Qual e o seu peso: '))
altura = float(input('Qual e a sua altura: '))

imc = peso / (altura ** 2)

print(f'O IMC dessa pessoa e de: {imc}')

if imc < 18.5: 
    print('Abaixo do Peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade morbida')
