# aça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m2.

alt = int(input("Altura: "))
lar = int(input("Largura: "))

print('Precisará de ', (2*(alt*lar)), 'litros de tinta')
