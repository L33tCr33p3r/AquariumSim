import pygame
class Fish:
    #parent class for all fish, unnecessary if all fish have the same behavior
    def __init__(self, LifeSpanMax, Width, Height, Speed, X, Y):
        self.age = 0 #is born, has lived no time.
        self.age_range = LifeSpanMax #use rng to decide when this fish will die of old age
        self.size = (Width, Height)
        self.speed = Speed
        self.x = X
        self.y = Y
        self.pos = (X,Y)
        self.color = (255,0,0)
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.pos,self.size))
        
        
class Salmon(Fish):
    def __init__(self, LifeSpanMax, Width, Height, Speed, X, Y):
        super().__init__(LifeSpanMax, Width, Height, Speed, X, Y) #this uses parent class constructor PLUS
        self.color = (255,103,51) #salmony color?                 #<-- this. 
        
class Tuna(Fish):
    def __init__(self, LifeSpanMax, Width, Height, Speed, X, Y):
        super().__init__(LifeSpanMax, Width, Height, Speed, X, Y)
        self.color = (255,51,101)