'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

print("Verificaremos se o número que sugerir é primo ou não. Tente um número de 1 a 1000.")
num = int(input("\nQual número? "))


if num > 1:
    primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        print("Primo")
    else:
        print("NÃO Primo 2")
else:
    print("NÃO Primo 1")
