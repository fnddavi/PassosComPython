#   Afim de tratar textos, segue alguns metodos e outros que são usados no tratamento de textos.
#   Os textos, como em muitas liguagens de programação, devem estar dentro de aspas


frase = 'Curso em Video Python'

#   Fatiamento: Colocar [] e dentro o indices que se deseja:
print(frase[9])
# Neste caso, será exibido apenas a letra "v" que está no indice 9

print(frase[9:13])
# Exibe os indices de 9 a 12 (13 é apenas o 'teto')

print(frase[:9])
# Exibe dos indices 0 a 9

print(frase[9:])
# Exibe dos indices 9 ao ultimo

print(frase[9:13:2])
# Exibe de (indices) 9 a 13 'pulando' de 2 em 2.

print(frase[9::3])
# Exibe de 9 ao ultimo indice 'pulando' de 3 em 3.

print(len(frase))
# função len() retorna o tamanho da variável em quantidade de caracteres

print(frase.count('o'))
# O método .cont() conta quantas vezes o caracter de parametro é encontrado na variável.

print(frase.count('o',0,13))
# Trará qntas vezes traz o 'o' e permite delimitar os indices que serão analisados (aqui de 0 a 13)

print(frase.find('deo'))
# Procura e traz em qual indice começa a sequencia de caracter estabelecida (aqui, "deo"). Se ocorrer mais de uma vez, será indicado também (?!)

print(frase.find('Fernando'))
# Considerando a frase, não será encontrado a sequencia de caracter pedido, então retornará o indice "-1" (não existe)

print('Curso' in frase)
# Deve retornar True caso encontre os caracteres pedidos ou False se não encontrar.

print(frase.replace('Python', 'Fernando'))
# método .replace faz a troca de strings onde procura pelo primeiro parametro e substitui pelo segundo parametro.

print(frase.upper())
# Transforma as str minusculas em maiusculas

print(frase.lower())
# Transforma as str maiusculas em minusculas

print(frase.capitalize())
# Transforma as str para minusculas e apenas a primeira letra do conjuto de str em maiuscula.

print(frase.title())
# Método que converte as str em minusculas e a primeira letra de cada palavra, após um espaço, em maiuscula

print(frase.strip())
# método que remove os espaços antes da primeira palavra e após a última palavra

print(frase.lstrip())
# método que remove os espaços A ESQUERDA da primeira palavra

print(frase.rstrip())
# método que remove os espaços A DIREITA da ultima palavra

print(frase.split())
# método que remove os espaços entre as palavras e as separa em uma lista

print(frase.split()[0])
# Neste caso, mostra a palavra que foi posta no indice 0 da lista

print('-'.join(frase))
# método que junta as palavras da lista com o caracter que está entre as aspas

# Alguns dos métodos mais comuns para manipulação de strings em Python:
 * len(): Retorna o tamanho da string.
 * lower(): Converte todas as letras da string para minúsculas.
 * upper(): Converte todas as letras da string para maiúsculas.
 * capitalize(): Converte a primeira letra da string para maiúscula e as demais para minúsculas.
 * count(): Conta o número de ocorrências de uma substring na string.
 * find(): Retorna a posição da primeira ocorrência de uma substring na string.
 * rfind(): Retorna a posição da última ocorrência de uma substring na string.
 * startswith(): Verifica se a string começa com uma substring específica.
 * endswith(): Verifica se a string termina com uma substring específica.
 * strip(): Remove espaços em branco do início e do fim da string.
 * replace(): Substitui todas as ocorrências de uma substring por outra na string.
 * split(): Divide a string em uma lista de strings com base em um delimitador.
 * join(): Une uma lista de strings em uma única string com base em um delimitador.