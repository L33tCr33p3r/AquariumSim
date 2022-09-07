import pygame
class BasicFishClass:
    #this class will hold basic data, and how it interacts with other fish
    def __init__(self ):#default constructor
        #this constructor isn't meant to be used
        #just to clearify what variables needed
        self.type = "string"
        self.age = 0
        self.age_range = 0 #use rng to decide life length (if not terminated by fish with predetor type

    def draw(self, screen):
        pygame.draw.rect(screen, (255,0,0), ((500,500),(50,50)))