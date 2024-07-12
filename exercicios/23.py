'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos
separados.
'''

num = int(input("Numero entre 0 e 9999: "));

if num < 0:
    print("Numero inválido!")
elif num > 9999:
    print("Numero inválido!")
else:
    num_para_string = str(num)
    print(type(num_para_string))

print(len(string))