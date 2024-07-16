'''
Faça um programa que leia uma frase pelo teclado e mostre:
(a) Quantas vezes aparece a letra "A".
(b) Em que posição ela aparece pela primeira vez.
(c) Em que posição ela aparece pela última vez.
'''

frase = input("Frase: ").lower()
print("Onde estão e qntas são as letras 'a'")
print("Quantidade: ", frase.count('a'), "Primeira: ", frase.find('a'), "Ultima: ", frase.rfind('a'))
