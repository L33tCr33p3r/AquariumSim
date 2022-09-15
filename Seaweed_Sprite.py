import pygame

class Seaweed():
    def __init__(self, XPos, YPos, mul):
        self.XPos = XPos
        self.YPos = YPos
        self.VertFramNum = 0
        self.HorzFramNum = 0
        self.mul = mul
        self.Sprite = pygame.image.load("Seaweed.png")
        self.Sprite = pygame.transform.scale(self.Sprite,(self.Sprite.get_width()*self.mul,self.Sprite.get_height()*self.mul))
        

    def draw(self, screen: pygame.Surface):
        screen.blit(self.Sprite, (self.XPos,self.YPos), ((self.HorzFramNum * 60 * self.mul, self.VertFramNum * 80 * self.mul), (60*self.mul, 80*self.mul)))

    
