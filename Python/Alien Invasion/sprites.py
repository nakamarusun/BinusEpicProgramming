""" all he sprites are here """

import pygame.sprite
import pygame.image
import pygame.rect
import random
import game_sprite_queue as GMque

class SpriteParent(pygame.sprite.Sprite):
    
    def __init__(self, image, coords, drawn):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = coords
        if drawn: GMque.addToQueue(self)
    
    def __del__(self):
        GMque.delFromQueue(self)

class Background(pygame.sprite.Sprite):

    def __init__(self, imageFile):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imageFile)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (0, 0)

class Fridge(SpriteParent):

    def __init__(self, coords):
        self.imageIdle = pygame.image.load("sprites/fridgeClosed.png")
        self.imageAttack = pygame.image.load("sprites/fridgeOpen.png")
        
        super().__init__(self.imageIdle, coords, True)

    def attack(self):
        pass

class Hand(SpriteParent):

    def __init__(self, coords):
        self.imageGoing = pygame.image.load("sprites/openHand.png")
        self.imageBack = pygame.image.load("sprites/closedHand.png")
        
        super().__init__(self.imageBack, coords, True)

    def going(self):
        pass

    def back(self):
        pass

class Fruits(SpriteParent):

    fruitsSprites = ("fruits1", "fruits2", "fruits3")

    def __init__(self, coords):
        self.image = pygame.image.load( "sprites/{sprite}".format(sprite=Fruits.fruitSprites[random.randint(0, 2)]) )

        super().__init__(self.image, coords, True)