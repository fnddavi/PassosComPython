'''
Refaça o exercício 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço FOR.
'''

nm = int(input('Numero: '))
for f in range(10):
    if f<11:
        print(f'{nm} x {f+1:2} = {nm*(f+1)}')
