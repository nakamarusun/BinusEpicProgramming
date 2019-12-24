""" used as a queue for sprites
before they are drawn to the screen """

import pygame.sprite
import sprites

drawQueue = []

def addToQueue(object):
    drawQueue.append(object)

def delFromQueue(object):
    for i in range(len(drawQueue)):
        if object == drawQueue[i]:
            drawQueue.pop(i)
            break

def mainDrawEvent(screen):
    for sprite in drawQueue:
        screen.blit(sprite.image, sprite.rect)