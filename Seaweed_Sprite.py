import pygame

class Seaweed():
    def __init__(self, XPos, YPos, VertFramNum, HorzFramNum, mul):
        self.XPos = XPos
        self.YPos = YPos
        self.VertFramNum = VertFramNum
        self.HorzFramNum = HorzFramNum
        self.mul = mul
        self.Sprite = pygame.image.load("Seaweed.png")
        self.Sprite = pygame.transform.scale(self.Sprite,(self.Sprite.get_width()*self.mul,self.Sprite.get_height()*self.mul))
        

    def draw(self, screen: pygame.Surface):
        screen.blit(self.Sprite, (self.XPos,self.YPos), ((self.HorzFramNum * 60 * self.mul, self.VertFramNum * 80 * self.mul), (60*self.mul, 80*self.mul)))

    
