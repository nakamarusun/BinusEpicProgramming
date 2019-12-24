import pygame.sprite
import pygame.image
import random

class Background(pygame.sprite.Sprite):

    def __init__(self, imageFile):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imageFile)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (0, 0)


class Fridge(pygame.sprite.Sprite):

    def __init__(self, coords):
        self.imageIdle = pygame.image.load("sprites/fridgeClosed.png")
        self.imageAttack = pygame.image.load("sprites/fridgeOpen.png")
        self.coords = coords

    def attack(self):
        pass

class Hand(pygame.sprite.Sprite):

    def __init__(self, coords):
        self.imageGoing = pygame.image.load("sprites/openHand.png")
        self.imageBack = pygame.image.load("sprites/closedHand.png")
        self.coords = coords

class Fruits(pygame.sprite.Sprite):

    fruitsSprites = ("fruits1", "fruits2", "fruits3")