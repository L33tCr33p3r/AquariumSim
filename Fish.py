import random
import pygame


class Fish:
    # parent class for all fish, unnecessary if all fish have the same behavior
    def __init__(self, LifeSpanMax, Width, Height, X, Y, screenX, screenY):
        self.age = 0  # is born, has lived no time.
        self.age_range = (
            LifeSpanMax  # use rng to decide when this fish will die of old age
        )
        self.width = Width
        self.height = Height
        self.x = X
        self.y = Y
        self.screenX = screenX
        self.screenY = screenY
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        self.turn()

    def turn(self):
        self.vx = random.random() + random.randint(-2, 1)
        self.vy = random.random() + random.randint(-2, 1)

    def update(self, screen):
        r = random.randint(1, 100)
        if r == 1:
            self.turn()
        self.collide()
        self.x += self.vx
        self.y += self.vy
        pygame.draw.rect(
            screen, self.color, ((self.x, self.y), (self.width, self.height))
        )

    def collide(self):
        # wall collision
        if self.x + self.width > self.screenX or self.x < 0:
            self.vx *= -1
        if self.y + self.height > self.screenY or self.y < 0:
            self.vy *= -1


class Salmon(Fish):
    def __init__(self, LifeSpanMax, Width, Height, X, Y):
        super().__init__(
            LifeSpanMax, Width, Height, X, Y
        )  # this uses parent class constructor PLUS
        self.color = (255, 103, 51)  # salmony color?                 #<-- this.


class Tuna(Fish):
    def __init__(self, LifeSpanMax, Width, Height, X, Y):
        super().__init__(LifeSpanMax, Width, Height, X, Y)
        self.color = (255, 51, 101)
