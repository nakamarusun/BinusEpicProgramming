""" used as a queue for sprites
before they are drawn to the screen """

import pygame.sprite

drawQueue = []

def addToQueue(object):
    drawQueue.append(object)

def delFromQueue(object):
    for i in range(len(drawQueue)):
        if object == drawQueue[i]:
            del drawQueue[i]
            break

def mainDrawEvent(screen):
    for sprite in drawQueue:
        screen.blit(sprite.image, sprite.rect)
        try:
            sprite.update()
        except NameError:
            pass
        except:
            raise SyntaxError("Failed running {obj_name}'s update function".format(obj_name=sprite) )