# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, radians, tan

ang = float(input("Angulo: "))
sen = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))

print(
    'Dado o angulo "{:.2f}", o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}.'.format(
        ang, sen, coss, tang
    )
)
