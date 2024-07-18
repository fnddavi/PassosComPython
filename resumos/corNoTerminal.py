'''
Instalar a biblioteca "Colorama":
    pip install colorama
'''

from colorama import Fore, Back, Style, init

init()

print(Fore.GREEN + 'Texto em verde' + Style.RESET_ALL)
print(Back.YELLOW + 'Fundo amarelo' + Style.RESET_ALL)
print(Fore.RED + Back.WHITE + 'Texto vermelho com fundo branco' + Style.RESET_ALL)