"""
Refaça o exercício 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: todos os  lados iguais é EQUILÁTERO; dois lados iguais é ISÓSCELES; todos os lados diferentes é ESCALENO.
"""

retas = []

for i in range(3):
    r = float(input(f"Reta {i+1}: "))
    retas.append(r)
r1, r2, r3 = retas

def form_triangle(r1,r2,r3):
    if ((r1 + r2) > r3) and ((r1 + r3) > r2) and ((r3 + r2) > r1):
        return True
    else:
        print('Nao e um triangulo')


seTriangulo = form_triangle(r1,r2,r3)
if seTriangulo:
    if (r1==r2) and (r2==r3) and (r3==r1):
        print('Triangulo equilatero')
    elif (r1==r2) or (r2==r3) or (r3==r1):
        print('Isosceles')
    else:
        print('Escaleno')
else:
    ('Houve um erro! Verifique e tente novamente.')