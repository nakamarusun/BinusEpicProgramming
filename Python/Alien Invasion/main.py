"""
Tugas terakhir for TA brenda
"""
import pygame
import pygame.display
import pygame.event
import pygame.sprite
import pygame.font
import time
from sys import exit
# Customs
import sprites
import event_loader as EVload
import game_functions as GMfun
import game_vars as GMvar


# Inits
pygame.init()
pygame.font.init()
pygame.display.set_caption("Food Invasion")

# Main loop
while True:

    startTime = time.time()     # Time marker
    EVload.loadEvents()         # Pump events and load them into EVload.curEvents list. IS A MUST.

    # Background draws
    GMvar.screen.blit(GMvar.background.image, GMvar.background.rect)

    # Main draws


    # FPS Calc
    GMfun.showFps(GMvar.screen, startTime)

    pygame.display.flip()