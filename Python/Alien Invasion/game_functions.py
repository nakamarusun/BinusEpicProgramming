""" custom game functions """


import pygame
import pygame.sprite
import pygame.event
import pygame.time
import game_vars as GMvar

from time import time

def showFps(screen, startFrame: float):
    try:
        FPS = "FPS: " + str(1/(time() - startFrame))
    except:
        FPS = "FPS: TOO HIGH"
    fpsText = GMvar.defFont.render(FPS, True, (0,0,0))
    screen.blit(fpsText, (0, 0))

def deltaTiming(fps: int, startFrame: float):
    frameDur = 1/fps
    pygame.time.delay( int((frameDur - (time()-startFrame)) * 1000) )

class Timer:
    def __init__(self, milisecond):
        self.end = time() + milisecond/1000

    def check(self):
        if time() > self.end:
            return True
            del self
        else:
            return False