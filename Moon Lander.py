import pygame
import os
pygame.init()
#Sets where the game screen will be
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20, 20) 

screen = pygame.display.set_mode((700, 1000))
game_status = True
pygame.display.set_caption("Lunar Lander Simulator")

doExit = False
clock = pygame.time.Clock()

#player position
xpos = 320
ypos = 100

#player variables
xVel = 0
yVel = 0
isOnGround = False
RocketOn = False
crashed = False

moveJump = False
moveLeft = False
moveRight = False

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
text1 = font.render('Vertical velocity: ', False, (0, 200, 200))
text2 = font.render(str(int(yVel)), 1, (0, 200, 200))
text3 = font.render('YOU CRASHED! ', False, (200, 50, 50))
text4 = font.render('Vertical velocity: ', False, (200, 20, 20))
text5 = font.render(str(int(yVel)), 1, (200, 20, 20))
text6 = font.render('Height: ', False, (20, 20, 200))
text7 = font.render(str(int(ypos)), 1, (20, 20, 200))

game_loop = True

while game_loop == True:
    delta = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
            
        #LEFT INPUT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveLeft = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveLeft = False
                
        #RIGHT INPUT

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveRight = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moveRight = False


        #UP INPUT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moveJump = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                moveJump = False
        
    #What happens when you crash    
    if isOnGround == True and abs(yVel) >.5:
        crashed = True
        screen.blit(text3,(200, 500))
        pygame.display.flip()
        pygame.time.wait(1000)
        xpos = 350
        ypos = 0
        xVel = 0
        yVel = 0
        isOnGround = False
    # else:
    #     yVel = 0
    #     xVel = 0

    if moveJump == True:
        yVel -= .417 * delta
        isOnGround = False
        RocketOn = True
        
    elif moveJump == False and ypos < 910:
        RocketOn = False
        if isOnGround == False:
            yVel += (delta)

    


    if moveLeft == True:
        xVel -= (delta)
    elif moveRight == True:
        xVel += (delta)
    else:
        xVel = 0


    if ypos > 950 and crashed:
        isOnGround = True
        yPos = 950



    xpos += xVel
    ypos += yVel

    text2 = font.render(str("%.2f" %(yVel * -1)), 1, (0, 200, 200))
    text5 = font.render(str("%.2f" %(yVel * -1)), 1, (200, 20, 20))
    text6 = font.render('Height: ', False, (20, 20, 200))
    text7 = font.render(str(int(1000-ypos)), 1, (20, 20, 200))

    screen.fill((0, 0, 0))    

    pygame.draw.rect(screen, (100, 0, 100),(xpos, ypos, 60, 20) )

    if abs(yVel) < .5:
        screen.blit(text1, (10, 10))
        screen.blit(text2, (250, 10))
    else:
        screen.blit(text4, (10, 10))
        screen.blit(text5, (250, 10))

    

    pygame.display.flip()
# END OF GAME LOOP------------------------------------------------------------------------------------------------
pygame.quit()
