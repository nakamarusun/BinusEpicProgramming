import pygame
import pygame.display
import pygame.font
from sprites import Background

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((800, 600))                    # Main screen
defFont = pygame.font.Font(pygame.font.get_default_font(), 12)  # Default debug font
background = Background("sprites/background.png")               # Background sprite