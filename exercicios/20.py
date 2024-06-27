# O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

alunos = []
for i in range(1, 5):
    aluno = input("Nome do/a aluno/a {}: ".format(i))
    alunos.append(aluno)

shuffle(alunos)

print("A ordem de apresentação será: {}".format(alunos))
