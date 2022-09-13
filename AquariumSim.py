'''Main File'''
import pygame
from Fish import *

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1920,1080)) #add screen scaling when in window mode
    #mouse vars
    MousePos = (0,0)

    Background = pygame.image.load("Background.png")
    
    running = True
    while running:
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
        #draw
        screen.blit(Background, (0,0))

        pygame.display.flip()
    pygame.quit()
