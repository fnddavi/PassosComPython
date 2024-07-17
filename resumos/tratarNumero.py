'''
Funções, bibliotecas e métodos usuais para tratar mumeros
'''

import random
# A biblioteca random fornece funções para gerar números aleatórios.

numero_aleatorio = random.randint(1, 10)  # Gera um número entre 1 e 10
# Você pode usar a função randint(inicio, fim) para gerar um número inteiro aleatório entre inicio e fim, incluindo ambos.

lista = [1, 2, 3, 4, 5, 6]
random.shuffle(lista)  # Embaralha a lista aleatoriamente
# Se você quiser gerar uma lista de números aleatórios, pode usar a função shuffle para embaralhar os elementos de uma lista existente.


numero_aleatorio = random.randrange(0, 10, 2)  # Gera números pares entre 0 e 9
# A função randrange é semelhante à função range. Ela gera um número aleatório dentro de um intervalo especificado

numeros_unicos = random.sample(range(1, 101), 10)  # Gera 10 números únicos entre 1 e 100
# A função sample permite gerar uma lista de valores únicos a partir de uma sequência

###

# Tipos de Números:
# Existem três tipos numéricos distintos em Python:
# Inteiros (int): Representam números inteiros sem parte decimal (por exemplo, 1, 10, -42).
# Números de Ponto Flutuante (float): Representam números reais com parte decimal (por exemplo, 1.2, 3.14159, -42.0).
# Números Complexos (complex): Têm uma parte real e uma imaginária.
# Operações Básicas:

# Você pode realizar operações matemáticas básicas com números:
'''
Adição: a + b
Subtração: a - b
Multiplicação: a * b
Divisão: a / b
Módulo (resto da divisão): a % b
Potenciação: a ** b
Divisão inteira: a // b
'''
#Arredondamento:
#Para arredondar números em Python:
'''
Arredondamento para o valor mais próximo: round(numero)
Arredondamento para um valor superior: math.ceil(numero)
Arredondamento para um valor inferior: math.floor(numero)
'''
# Funções Matemáticas:
# A biblioteca math oferece funções matemáticas adicionais, como math.sin(), math.cos(), math.sqrt(), etc.

# Verificação de Tipo:
# Use a função type(variavel) para verificar o tipo de uma variável.
# A função isinstance(variavel, tipo) verifica se uma variável é do tipo especificado.