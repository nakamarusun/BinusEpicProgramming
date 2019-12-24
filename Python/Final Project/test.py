from time import sleep
import pygame
import math
import random
 
pygame.init()
screen = pygame.display.set_mode((1280, 720))
done = False
is_blue = True
x = 30
y = 30

r: int = 255
g: int = 0
b: int = 255

speed = [9,9]

time = 0

while not done:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                    done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    is_blue = not is_blue
         
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 1
        if pressed[pygame.K_DOWN]: y += 1
        if pressed[pygame.K_LEFT]: x -= 1
        if pressed[pygame.K_RIGHT]: x += 1

        if r == 255:
            g += 1
            b -= 1
        if g == 255:
            b += 1
            r -= 1
        if b == 255:
            r += 1
            g -= 1

        if x < 0 or x > 1280:
            speed[0] = -speed[0]
        if y < 0 or y > 720:
            speed[1] = -speed[1]

        x += speed[0]
        y += speed[1]

        time += 1

        if is_blue: color = (r, g, b)
        else: color = (255, 100, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 5, 5))
        sleep(0.001)
        pygame.display.flip()