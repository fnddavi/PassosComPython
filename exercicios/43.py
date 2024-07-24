'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, onde: abaixo de 18,5 é ABAIXO DO PESO; entre 18.5 e 25 é PESO IDEAL; 25 até 30 é SOBREPESO; 30 até 40 é OBESIDADE; acima de 40 é OBESIDADE MÓRBIDA
'''


usr_peso = float(input('Qual o peso? '))
usr_alt = float(input("Qual a Altura? "))

#
imc = (usr_peso/(usr_alt**2))
print(f'IMC em: {imc:.2f}')

if imc < 18.5:
    print("Abaixo")
elif imc >= 18.5 and imc < 25:
    print("Ideal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif imc >= 30 and imc < 40:
    print("Obesidade")
else:
    print("Obesidade morbida")