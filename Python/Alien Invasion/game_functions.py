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
    overText = pygame.font.Font(pygame.font.get_default_font(), 64).render("GAME OVER", True, (0,0,0))
    overScreen = pygame.font.Font(pygame.font.get_default_font(), 24).render( "Score: {}".format(str(GMque.drawQueue[0].score)) , True, (0,0,0))
    high = ""
    try:
        with open("High.save", "r+", encoding="utf-8") as file:
            high = file.readline()
    except:
        with open("High.save", "w+", encoding="utf-8") as file:
            file.write(str(GMque.drawQueue[0].score))
            high = str(GMque.drawQueue[0].score)
    print(high)
    if int(high) < GMque.drawQueue[0].score:
        with open("High.save", "w+", encoding="utf-8") as file:
            file.write(str(GMque.drawQueue[0].score))
            high = str(GMque.drawQueue[0].score)
    GMque.drawQueue = []
    highScreen = pygame.font.Font(pygame.font.get_default_font(), 24).render( "High Score: {}".format(str(high)) , True, (0,0,0))
    Blitter(overText, (180, 280))
    Blitter(overScreen, (330, 340))
    Blitter(highScreen, (300, 367))

class Timer:
    def __init__(self, milisecond):
        self.end = time() + milisecond/1000

    def check(self):
        if time() > self.end:
            return True
            del self
        else:
            return False