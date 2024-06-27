# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

from random import choice

aluno1 = input("Nome do/a aluno/a 1: ")
aluno2 = input("Nome do/a aluno/a 2: ")
aluno3 = input("Nome do/a aluno/a 3: ")
aluno4 = input("Nome do/a aluno/a 4: ")

alunos = [aluno1, aluno2, aluno3, aluno4]
escolha = choice(alunos)

print("O aluno escolhido foi: {}".format(escolha))

# print(' Ou, fazemos assim:')

alunos = []
for i in range(1, 5):
    aluno = input("Nome do/a aluno/a {}: ".format(i))
    alunos.append(aluno)
escolha = choice(alunos)

print("O aluno escolhido foi: {}".format(escolha))
