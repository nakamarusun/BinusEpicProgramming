""" used to store all game vars
"""


import pygame
import pygame.display
import pygame.font
import pygame.sprite
import pygame.image

pygame.init()
pygame.font.init()

size = (800, 600)

screen = pygame.display.set_mode(size)                          # Main screen
defFont = pygame.font.Font(pygame.font.get_default_font(), 12)  # Default debug font
background = pygame.image.load("sprites/background.png")        # Background sprite