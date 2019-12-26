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
import game_sprite_queue as GMque


# Inits
pygame.init()
pygame.font.init()
pygame.display.set_caption("Food Invasion")

# Game creation code
fridge = sprites.Fridge( (GMvar.size[0]/2 - 39, GMvar.size[1] - 188) )

# Main loop
while True:

    startTime = time.time()     # Time marker
    EVload.loadEvents()         # Pump events and load them into EVload.curEvents list. IS A MUST.

    # Background draws
    GMvar.screen.blit(GMvar.background, (0, 0) )

    # Update and draw
    GMque.mainDrawEvent(GMvar.screen)
    
    GMfun.showFps(GMvar.screen, startTime)  # FPS Calc
    GMfun.deltaTiming(60, startTime)        # Delta timing
    pygame.display.flip()