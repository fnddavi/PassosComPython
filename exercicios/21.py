# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
import time

# Inicializa o pygame
pygame.init()

# Inicializa o mixer de música
# pygame.mixer.init()

# Carrega o arquivo MP3
pygame.mixer.music.load("../02 - Abertura.mp3")

# Reproduz o arquivo MP3
pygame.mixer.music.play()

# Mantém o programa rodando até que a música termine
while pygame.mixer.music.get_busy():
    time.sleep(1)
