'''Main File'''
import pygame
import random
from Fish import *
from Seaweed_Sprite import *


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1920,1080)) #add screen scaling when in window mode
    #mouse vars
    MousePos = (0,0)

    Background = pygame.image.load("Background.png")

    seaweedList = []
    numOfSw = random.randint(7,14)
    #XSpacing = 1850//numOfSw
    for i in range(numOfSw):
        mul = (random.randint(3, 7))
        seaweedList.append(Seaweed((random.randint(10,(1910-(60*mul)))),(random.randint(1045, 1080)-(80*mul)),mul))
        #seaweedList.append(Seaweed((random.randint((10+(XSpacing*i)), ((10+XSpacing)+(XSpacing*i)))),(random.randint(1045, 1080)-(80*mul)),mul))
        #(random.randint((10+(XSpacing*numOfSw)), ((10+XSpacing)+(XSpacing*numOfSw))))
        #random.randrange(10,1910,random.randint(XSpacing*i,XSpacing*i+XSpacing))
    
    running = True
    while running:
        screen.blit(Background, (0,0))
        #game loop, instantiate some fish in another file.
        for event in pygame.event.get():#event loop here
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LCTRL]:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                MousePos = pygame.mouse.get_pos()#gets mouse pos
                pygame.draw.circle(screen,(255,255,255),(MousePos),50)

        for i in range(len(seaweedList)):
            seaweedList[i].draw(screen)

        pygame.display.flip()
    pygame.quit()
