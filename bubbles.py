from ast import BitXor
import pygame
import random

# spawnPoint = 0

class Bubles:
    bx = 0
    by = 0

    def update(self, screen: pygame.Surface):
        self.by -= 8
        screen.blit(self.Sprite,(self.bx, self.by))
        #pygame.draw.circle(screen, (200, 200, 255), (self.bx, self.by), 10)

    def should_delete(self, screen:pygame.Surface) -> bool:
        return not screen.get_rect().collidepoint(self.bx, self.by)
    
    def __init__(self, spawnpoint: int, screenY):
        self.bx = spawnpoint + random.randint(-75, 75)
        self.by = screenY
        self.Sprite = pygame.image.load("Bubble.png")

        
        

# screen = pygame.display.set_mode((1920,1080))



# interval: float = 10
# starttime = pygame.time.get_ticks()
# # every frame:
# if pygame.time.get_ticks() - starttime <= 1000 * interval:
#     starttime = pygame.time.get_ticks()
#     spawnPoint = random.randint(100,1820)
#     print('adss')

# while True:
#     if (1000 * interval) % 1000 == 0:
#         print('ssssssss')
#     Bubles(spawnPoint)
    
#     # this will make this frame last forever