'''Main File'''
import pygame
from Fish import *
from bubbles import Bubles

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1920,1080))
    MousePos = (0,0)
    
    fishies = list()
    for i in range(25):
        fishies.append(Fish(120,random.randint(25,100),random.randint(25,100),random.randint(100, 1820), random.randint(100,980)))

    bubles = list()


    Background = pygame.image.load("Background.png")

    interval: float = 10
    spawnPoint: int = random.randint(100,1820)
    spawnPoint2: int = random.randint(100,1820)
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
        
        if pygame.time.get_ticks() % (1000 * interval) < 30: # declan: this code is really stupid, it should be better, but this is easier to write. Eli: nah
            spawnPoint = random.randint(100,1820)
        if pygame.time.get_ticks() % (1000 * (interval / 15)) < 30: # declan: this code is really stupid, it should be better, but this is easier to write. Eli: nah
            bubles.append(Bubles(spawnPoint))

        if pygame.time.get_ticks() % (1200 * interval) < 29: # declan: this code is really stupid, it should be better, but this is easier to write. Eli: nah
            spawnPoint2 = random.randint(100,1820)
        if pygame.time.get_ticks() % (1000 * (interval / 20)) < 30: # declan: this code is really stupid, it should be better, but this is easier to write. Eli: nah
            bubles.append(Bubles(spawnPoint2))

        for f in fishies:
            f.update(screen)
            
        for b in bubles:
            b.update(screen)
            if b.should_delete(screen):
                bubles.remove(b)
                del b

        pygame.display.flip()
    pygame.quit()
