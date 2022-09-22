'''Main File'''
import pygame
import random
from Fish import *
from Seaweed_Sprite import *


if __name__ == '__main__':
    pygame.init()
    screenX = 1920
    screenY = 1080
    screen = pygame.display.set_mode((screenX,screenY)) #add screen scaling when in window mode
    
    MousePos = (0,0)
    groundHeight = 35
    FrameSizeX = 15
    FrameSizeY = 60

    Background = pygame.image.load("Background.png")

    seaweedList = []
    numOfSw = random.randint(10,21)
    for i in range(numOfSw):
        mul = (random.randint(3, 7))
        seaweedList.append(Seaweed((random.randint(10,(screenX-(FrameSizeX*mul)))),(random.randint(screenY - groundHeight, screenY)-(FrameSizeY*mul)),mul))

    clock = pygame.time.Clock()
    
    frameRate = 60
    frameRateNum = 0
    running = True
    while running:
        clock.tick(frameRate)
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

        for i in seaweedList:
            i.draw(screen,frameRateNum)

        frameRateNum += 1
        if frameRateNum >= frameRate:
            frameRateNum = 0
        pygame.display.flip()
    pygame.quit()
