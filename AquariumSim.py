import pygame as py
# This file will be main. 
# Initialize pygame here 


#       Make sure to keep it organized 
#       
#       At the top of files make sure to provide a brief, and informative description of it's purpose 
#
#globals
py.init()
screen = py.display.set_mode([1000,1000])#add screen scaling when in window mode
#mouse vars
MousePos = [0,0]


doExit = False
while doExit ==false:
    #game loop, instantiate some fish in another file.
    for event in pygame.event.get():#event loop here
            if event.type == QUIT:
               pygame.quit()
               return
            elif event.type == py.KEYDOWN:
                MousePos = pygame.key.get_pressed()#gets mouse pos
               #click 
    #draw section/IO