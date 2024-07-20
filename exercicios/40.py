"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma
mensagem no final, de acordo com a média atingida: média abaixo de 5,0 é REPROVADO;
média entre 5,0 e 6,9 fica de RECUPERAÇÃO; média 7,0 ou superior é APROVADO.
"""

notas = []

for i in range(2):
    nota = float(input(f"Nota {i+1}: \n"))
    notas.append(nota)
nota1, nota2 = notas

media = (nota1 + nota2) / (len(notas))
print("Média:", media)

if media < 5:
    print("Aluno(a) retido(a)")

elif 5 >= media <= 6.9:
    print("Aluno/a de RECUPERAçãO")

else:
    print("Aluno/a APROVADO/A!")
