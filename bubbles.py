from ast import BitXor
import pygame
import random

# spawnPoint = 0

class Bubles:
    bx = 0
    by = 0

    def update(self, screen: pygame.Surface):
        self.by -= 8
        pygame.draw.rect(screen, (200, 200, 255), pygame.Rect(self.bx, self.by, 20, 20))

    def should_delete(self, screen:pygame.Surface) -> bool:
        return not screen.get_rect().collidepoint(self.bx, self.by)
    
    def __init__(self, spawnpoint: int):
        self.bx = spawnpoint + random.randint(-75, 75)
        self.by = 1080

        
        

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