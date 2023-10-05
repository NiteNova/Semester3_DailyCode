import pygame
import random
pygame.init()
pygame.display.set_caption("Platformer with inheritance")
screen = pygame.display.set_mode((800, 800))
screen.fill((0,0,0))
clock = pygame.time.Clock()
gameover = False

LEFT= 0
RIGHT= 1
UP = 2
keys = [False, False, False]

vx = 0
vy = 0

class player():
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isOnGround = False
        self.vy = 0
        self.vx = 0
    def draw(self):
        pygame.draw.rect(screen, (100, 200, 100), (self.xpos, self.ypos, 20, 40))
    def move(self, keys):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: #keyboard input
                if event.key == pygame.K_LEFT:
                    keys[LEFT]=True

                elif event.key == pygame.K_UP:
                    keys[UP]=True
                
                elif event.key == pygame.K_RIGHT:
                    keys[RIGHT]=True
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    keys[LEFT]=False

                elif event.key == pygame.K_UP:
                    keys[UP]=False

                elif event.key == pygame.K_RIGHT:
                    keys[RIGHT]=False
            
        if keys[RIGHT]==True:
            self.vx=+.3
        
        #LEFT MOVEMENT
        elif keys[LEFT]==True:
            self.vx=-.3
        #turn off velocity
        else:
            self.vx = 0
            #JUMPING
        if keys[UP] == True and p1.isOnGround == True: #only jump when on the ground
            self.vy = -2
            self.isOnGround = False
        
        if self.ypos > 760:
            self.isOnGround = True
            self.vy = 0
            self.ypos = 760

        if self.isOnGround == False:
            self.vy += .2
    
        self.xpos += self.vx
        self.ypos += self.vy


            

p1 = player(50, 600)

class platform():
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos 

    def draw(self):
        pygame.draw.rect(screen, (100, 50, 100), (self.xpos, self.ypos, 80, 30))
    
    def move(self):
        pass

class IceBlock(platform):
    def draw(self):
        pygame.draw.rect(screen, (0, 120, 150), (self.xpos, self.ypos, 80, 30))
    
class TrampBlock(platform):
    def draw(self):
        pygame.draw.rect(screen, (0, 120, 20), (self.xpos, self.ypos, 80, 30))

class BreakBlock(platform):
    def draw(self):
        pygame.draw.rect(screen, (150, 75, 0), (self.xpos, self.ypos, 80, 30))

class MovingBlock(platform):
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.startX = self.xpos
        self.startY = self.ypos
        self. direction = 1

    def draw(self):
        pygame.draw.rect(screen, (200, 50, 100), (self.xpos, self.ypos, 80, 30))

    def move(self):
        if self.direction == 1:
            if self.xpos < self.startX:
                self.direction*= -1
            else:
                self.xpos-=.1
        else:
            if self.xpos > self.startX+200:
                self.direction *= -1
            else:
                self.xpos+=.1


plats = []
for i in range(2):
    plats.append(platform(random.randrange(50, 700), random.randrange(50, 700)))
for i in range(2):
    plats.append(MovingBlock(random.randrange(50, 500), random.randrange(50, 500)))
for j in range(2):
    plats.append(IceBlock(random.randrange(100, 700), random.randrange(120, 500)))
for j in range(2):
    plats.append(TrampBlock(random.randrange(150, 650), random.randrange(120, 600)))
for j in range(2):
    plats.append(BreakBlock(random.randrange(50, 700), random.randrange(50, 650)))

while gameover == False:
    

    p1.move(keys)

    for i in range(len(plats)):
            plats[i].move()
    #le render section
    screen.fill((0, 0, 0))
    for i in range(len(plats)):
        plats[i].draw()

    p1.draw()
    pygame.display.flip()

pygame.quit()
