""" Used to load all events from SDL, and put it
inside a list """


import pygame
import pygame.event

curEvents = []

def loadEvents():

    # So that the pointer stays the same
    num = len(curEvents)
    for i in range(num):
        curEvents.pop(0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        curEvents.append(event)