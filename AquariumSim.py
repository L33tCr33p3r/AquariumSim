import pygame
# This file will be main. 
# Initialize pygame here 


#       Make sure to keep it organized 
#       
#       At the top of files make sure to provide a brief, and informative description of it's purpose 
#
#globals
pygame.init()
screen = pygame.display.set_mode((1920,1080))#add screen scaling when in window mode
#mouse vars
MousePos = (0,0)


running = True
while running:
    #game loop, instantiate some fish in another file.
    for event in pygame.event.get():#event loop here
            if event.type == pygame.QUIT:
               running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                MousePos = pygame.mouse.get_pos()#gets mouse pos
               #click 
    #draw section/IO
    
pygame.quit()