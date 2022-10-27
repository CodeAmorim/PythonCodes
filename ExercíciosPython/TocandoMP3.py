# Tocar um mp3 usando o PyGames
import pygame

pygame.init()
pygame.mixer.music.load('mp3.mp3')
pygame.mixer.music.play()
pygame.event.wait()