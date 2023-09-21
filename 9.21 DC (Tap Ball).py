import pygame
pygame.init()

screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("bootleg shots")

bx = 980
by = 200


constantly_move = True
doExit = False
press = False
xpos = 100
ypos = 730
xVel = 0
yVel = 0
timer = 0


clock = pygame.time.Clock()

while not doExit:   #Game Loop------------------------------Place holder
    #Event stuff
    delta = clock.tick(60) / 1000
    for event in pygame.event.get(): # game input
        if event.type == pygame.QUIT:
            doExit = True
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            press = True
            

        elif event.type == pygame.MOUSEBUTTONUP:
            press = False
            
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
            
            
    #position is updated by velocity
    xpos += xVel
    ypos += yVel        
            
    
    if xpos > 1020:
        xpos = -20
    if constantly_move == True:
        xpos += 2
            
    #movement
    if press == True:
        yVel = -12
    elif press == False and ypos <= 950:
        yVel = 4
    elif ypos >= 950 :
        yPos = 950
        yVel = 0
   
          
        

    
        
    #reflections paddle
    if xpos >= 980 and ypos >= 200 and ypos <= 300 and xpos <= 1000:
        constantly_move = False
        yVel *= -1
        xVel *= -1

    


    
    #render section
    
    screen.fill((0, 0, 0))
    
    pygame.draw.circle(screen,(255, 50, 0), (xpos, ypos), 15)
    
    pygame.draw.rect(screen, (255, 255, 255), (bx, by, 20, 100), 1)
    
    
    
    pygame.display.flip()
#End of game loop
pygame.quit()
