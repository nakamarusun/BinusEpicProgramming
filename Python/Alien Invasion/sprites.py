""" all he sprites are here """

import pygame.sprite
import pygame.image
import pygame.rect
import pygame.key
import random
import math

import game_sprite_queue as GMque
import event_loader as EVload
import game_functions as GMfun

class SpriteParent(pygame.sprite.Sprite):
    
    def __init__(self, image, coords, drawn):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = coords
        if drawn: GMque.addToQueue(self)
    
    def deleteSelf(self):
        GMque.delFromQueue(self)
        del self

    def __del__(self):
        GMque.delFromQueue(self)

class Fridge(SpriteParent):

    def __init__(self, coords):
        self.imageIdle = pygame.image.load("sprites/fridgeClosed.png")
        self.imageAttack = pygame.image.load("sprites/fridgeOpen.png")
        self.timerFruit = None
        
        super().__init__(self.imageIdle, coords, True)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.left -= 1
        if keys[pygame.K_RIGHT] and self.rect.left < 800 - 78:
            self.rect.left += 1
        if keys[pygame.K_SPACE]:
            self.image = self.imageAttack

        # Timer to create fruits
        if self.timerFruit == None:
            self.timerFruit = GMfun.Timer(random.randint(1000, 6000))
        else:
            if self.timerFruit.check():
                Fruits( (random.randint(0, 700), 20) )
                self.timerFruit = None

        for event in EVload.curEvents:
            if event.type == pygame.KEYUP:
                
                # Change sprite back to normal
                if event.key == pygame.K_SPACE:
                    self.image = self.imageIdle

            if event.type == pygame.KEYDOWN:

                # Attack script
                if event.key == pygame.K_SPACE:
                    handCount = 0

                    for queue in GMque.drawQueue:
                        if queue.__class__.__name__ == "Hand": handCount += 1
                    
                    if handCount < 3:
                        Hand( ((self.rect.left + (self.rect.width / 2)) - 110, (self.rect.top + (self.rect.height / 2)) - 123) )

class Hand(SpriteParent):

    def __init__(self, coords):
        self.imageGoing = pygame.image.load("sprites/openHand.png")
        self.imageBack = pygame.image.load("sprites/closedHand.png")
        self.going = True
        
        super().__init__(self.imageGoing, coords, True)

    def update(self):
        if self.going:
            self.rect.top -= 2
            if self.rect.top + self.rect.height < 0:
                self.deleteSelf()

            for sprite in GMque.drawQueue:
                if sprite.__class__.__name__ == "Fruits":
                    if pygame.sprite.collide_rect(self, sprite):
                        sprite.deleteSelf()
                        self.going = False
        else:
            self.image = self.imageBack
            for sprite in GMque.drawQueue:
                if sprite.__class__.__name__ == "Fridge":
                    deltay = self.rect.top - sprite.rect.top
                    deltax = self.rect.left - sprite.rect.left
                    direction = math.atan2(deltay, deltax)
                    self.rect.top += 2 * -math.sin(direction)
                    self.rect.left += 2 * -math.cos(direction)
                    if self.rect.top > 400:
                        self.deleteSelf()

class Fruits(SpriteParent):

    fruitsSprites = ("fruits1", "fruits2", "fruits3")

    def __init__(self, coords):
        self.image = pygame.image.load( "sprites/{sprite}.png".format(sprite=Fruits.fruitsSprites[random.randint(0, 2)]) )
        self.speed = random.randint(1,2)

        super().__init__(self.image, coords, True)

    def update(self):
        self.rect.left += self.speed
        if self.rect.left < 0 or self.rect.left + self.rect.width > 800:
            self.speed *= -1
            self.rect.top += 30