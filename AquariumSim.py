'''Main File'''
import pygame
import random
from Fish import *
from Seaweed_Sprite import *
from bubbles import *

if __name__ == '__main__':
    pygame.init()
    screenX = 1920
    screenY = 1080
    screen = pygame.display.set_mode((screenX,screenY)) #add screen scaling when in window mode
    
    MousePos = (0,0)
    groundHeight = 35
    FrameSizeX = 15
    FrameSizeY = 60
    
    fishies = list()
    for i in range(25):
        fishies.append(Fish(120,random.randint(25,100),random.randint(25,100),random.randint(100, 1820), random.randint(100,980)))
    
    seaweedList = []
    numOfSw = random.randint(10,21)
    for i in range(numOfSw):
        mul = (random.randint(3, 7))
        seaweedList.append(Seaweed((random.randint(10,(screenX-(FrameSizeX*mul)))),(random.randint(screenY - groundHeight, screenY)-(FrameSizeY*mul)),mul))
    
    Background = pygame.image.load("Background.png")
    
    interval: float = 10
    spawnPoint: int = random.randint(100,1820)
    spawnPoint2: int = random.randint(100,1820)
    
    clock = pygame.time.Clock()
    
    frameRate = 60
    frameRateNum = 0
    running = True
    while running:
        clock.tick(frameRate)
        screen.blit(Background, (0,0))
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LCTRL]:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                MousePos = pygame.mouse.get_pos()
                pygame.draw.circle(screen,(255,255,255),(MousePos),50)

        for i in seaweedList:
            i.draw(screen,frameRateNum)

        frameRateNum += 1
        frameRateNum % frameRate
        
        if pygame.time.get_ticks() % (1000 * interval) < 30: # declan: this code is really stupid, it should be better, but this is easier to write. Eli: nah
            spawnPoint = random.randint(100,1820)
        if pygame.time.get_ticks() % (1000 * (interval / 15)) < 30: # declan: this code is really stupid, it should be better, but this is easier to write. Eli: nah
            fishies.append(Bubles(spawnPoint))

        if pygame.time.get_ticks() % (1200 * interval) < 29: # declan: this code is really stupid, it should be better, but this is easier to write. Eli: nah
            spawnPoint2 = random.randint(100,1820)
        if pygame.time.get_ticks() % (1000 * (interval / 20)) < 30: # declan: this code is really stupid, it should be better, but this is easier to write. Eli: nah
            fishies.append(Bubles(spawnPoint2))

        for f in fishies:
            f.update(screen)
            if type(f) == Bubles and f.should_delete(screen):
                fishies.remove(f)
                del f
        pygame.display.flip()
    pygame.quit()
