import pygame
import random


class Bubble:
    bx = 0
    by = 0

    def update(self, screen: pygame.Surface):
        self.by -= 8

        screen.blit(self.Sprite, (self.bx, self.by))

    def should_delete(self, screen: pygame.Surface) -> bool:
        return not screen.get_rect().collidepoint(self.bx, self.by)

    def __init__(self, spawnpoint: int, screenY):
        self.bx = spawnpoint + random.randint(-75, 75)
        self.by = screenY
        self.Sprite = pygame.image.load("Assets\Images\Bubble.png")
