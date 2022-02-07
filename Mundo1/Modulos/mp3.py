import pygame #um dos modulos

pygame.init()
pygame.mixer.music.load('mp3.mp3')
pygame.mixer.music.play()
pygame.event.wait()