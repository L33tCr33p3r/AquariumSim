import pygame
import random


class Seaweed:
    def __init__(self, XPos, YPos, Multiplier):
        self.XPos = XPos
        self.YPos = YPos
        self.VertFramNum = 0
        self.HorzFramNum = 0
        self.Multiplier = Multiplier
        self.SpritX = 15
        self.SpritY = 60
        self.NumberOfFrames = 9
        self.FrameNum = random.randint(0, self.NumberOfFrames)
        self.FrameRates = [10, 12, 15, 20]
        self.Sprite = pygame.image.load("Assets\Images\SeaweedSheet.png")
        self.Sprite = pygame.transform.scale(
            self.Sprite,
            (
                self.Sprite.get_width() * self.Multiplier,
                self.Sprite.get_height() * self.Multiplier,
            ),
        )

    def draw(self, screen: pygame.Surface, frameRateNum):
        if (frameRateNum % self.FrameRates[random.randint(0, 3)]) == 0:
            self.FrameNum += 1
            if self.FrameNum > self.NumberOfFrames:
                self.FrameNum = 0

        screen.blit(
            self.Sprite,
            (self.XPos, self.YPos),
            (
                (self.FrameNum * self.SpritX * self.Multiplier, 0),
                (self.SpritX * self.Multiplier, self.SpritY * self.Multiplier),
            ),
        )
