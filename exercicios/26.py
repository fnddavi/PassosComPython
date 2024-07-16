'''
Faça um programa que leia uma frase pelo teclado e mostre:
(a) Quantas vezes aparece a letra "A".
(b) Em que posição ela aparece pela primeira vez.
(c) Em que posição ela aparece pela última vez.
'''

frase = input("Frase: ").lower()
letraA = frase.count('a')
letraFim = frase.rfind('a')
letraIni = frase.find('a')

print(f"A letra 'a' aparece {letraA} vezes no texto inserido, pela primeira vez na posição {letraIni} e pela última vez na posição {letraFim}")