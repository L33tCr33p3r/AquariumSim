'''Main File'''
import pygame
from Fish import *

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1920,1080))
    MousePos = (0,0)
    
    fishies = list()
    for i in range(25):
        fishies.append(Fish(120,random.randint(25,100),random.randint(25,100),random.randint(100, 1820), random.randint(100,980)))

    Background = pygame.image.load("Background.png")
    
    running = True
    while running:
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
                
        for f in fishies:
            f.update(screen)

        pygame.display.flip()
    pygame.quit()
