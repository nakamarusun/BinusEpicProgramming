""" custom game functions """


import pygame
import pygame.sprite
import pygame.event
import pygame.time
import pygame.font
import game_vars as GMvar
import game_sprite_queue as GMque

from time import time


class Blitter:
    def __init__(self, blitObject, coords):
        self.image = None
        self.object = blitObject
        self.coords = coords
        GMque.addToQueue(self)

    def update(self):
        GMvar.screen.blit(self.object, self.coords)

def showFps(screen, startFrame: float):
    try:
        FPS = "FPS: " + str(1/(time() - startFrame))
    except:
        FPS = "FPS: TOO HIGH"
    fpsText = GMvar.defFont.render(FPS, True, (0,0,0))
    screen.blit(fpsText, (0, 0))

def deltaTiming(fps: int, startFrame: float):
    frameDur = 1/fps
    delay = int((frameDur - (time()-startFrame)) * 1000)
    if delay > 0:
        pygame.time.delay( delay )

def gameOver():
    pygame.font.init()
    gameOverFont = pygame.font.Font(pygame.font.get_default_font(), 64)
    overText = gameOverFont.render("GAME OVER", True, (0,0,0))
    GMque.drawQueue = []
    Blitter(overText, (300, 280))

class Timer:
    def __init__(self, milisecond):
        self.end = time() + milisecond/1000

    def check(self):
        if time() > self.end:
            return True
            del self
        else:
            return False