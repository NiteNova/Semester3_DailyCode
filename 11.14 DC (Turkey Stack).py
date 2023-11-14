import pygame
from random import randrange as rr
from pygame.math import Vector2

screen = pygame.display.set_mode((800, 800))
exit = False
clock = pygame.time.Clock()

class Turkey():
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos,ypos)
        self.vy = 5
        self.vy2 = 10
        self.num = rr(0,2)
    
    def draw(self):
        if self.num == 0:
            #Feathers
            pygame.draw.circle(screen, (255, 165, 0), (self.pos.x+5, self.pos.y), 10)
            pygame.draw.circle(screen, (255, 165, 0), (self.pos.x+15, self.pos.y-22), 10)
            pygame.draw.circle(screen, (255, 165, 0), (self.pos.x+35, self.pos.y-35), 10)
            pygame.draw.circle(screen, (255, 165, 0), (self.pos.x+55, self.pos.y-22), 10)
            pygame.draw.circle(screen, (255, 165, 0), (self.pos.x+65, self.pos.y), 10)
            pygame.draw.circle(screen, (255, 165, 0), (self.pos.x+9, self.pos.y-11), 10)
            pygame.draw.circle(screen, (255, 165, 0), (self.pos.x+25, self.pos.y-30), 10)
            pygame.draw.circle(screen, (255, 165, 0), (self.pos.x+45, self.pos.y-30), 10)
            pygame.draw.circle(screen, (255, 165, 0), (self.pos.x+45, self.pos.y-30), 10)
            pygame.draw.circle(screen, (255, 165, 0), (self.pos.x+60, self.pos.y-11), 10)

            #Legs
            pygame.draw.rect(screen, (196, 180, 84), (self.pos.x+20, self.pos.y+10, 10, 30))
            pygame.draw.rect(screen, (196, 180, 84), (self.pos.x+40, self.pos.y+10, 10, 30))

            #Body
            pygame.draw.circle(screen, (139,69,19), (self.pos.x+35, self.pos.y), 30)
            pygame.draw.ellipse(screen, (139,69,19), (self.pos.x+23, self.pos.y-40, 25, 40))
            #Face
            pygame.draw.polygon(screen, (218,165,32), ((self.pos.x+30, self.pos.y-30), (self.pos.x+35, self.pos.y-15), (self.pos.x+41, self.pos.y-30)))
            pygame.draw.circle(screen, (255, 255, 255), (self.pos.x+28, self.pos.y-30), 5)
            pygame.draw.circle(screen, (0, 0, 0), (self.pos.x+28, self.pos.y-30), 3)
            pygame.draw.circle(screen, (255, 255, 255), (self.pos.x+43, self.pos.y-30), 5)
            pygame.draw.circle(screen, (0, 0, 0), (self.pos.x+43, self.pos.y-30), 3)
        else:
            #Feathers
            pygame.draw.circle(screen, (165, 42, 42), (self.pos.x+5, self.pos.y), 20)
            pygame.draw.circle(screen, (165, 42, 42), (self.pos.x+30, self.pos.y-32), 20)
            pygame.draw.circle(screen, (165, 42, 42), (self.pos.x+65, self.pos.y-55), 20)
            pygame.draw.circle(screen, (165, 42, 42), (self.pos.x+100, self.pos.y-32), 20)
            pygame.draw.circle(screen, (165, 42, 42), (self.pos.x+120, self.pos.y), 20)
            pygame.draw.circle(screen, (165, 42, 42), (self.pos.x+15, self.pos.y-15), 20)
            pygame.draw.circle(screen, (165, 42, 42), (self.pos.x+45, self.pos.y-45), 20)
            pygame.draw.circle(screen, (165, 42, 42), (self.pos.x+90, self.pos.y-45), 20)
            pygame.draw.circle(screen, (165, 42, 42), (self.pos.x+115, self.pos.y-12), 20)

            #Legs
            pygame.draw.rect(screen, (196, 180, 84), (self.pos.x+40, self.pos.y+10, 20, 60))
            pygame.draw.rect(screen, (196, 180, 84), (self.pos.x+70, self.pos.y+10, 20, 60))

            #Body
            pygame.draw.circle(screen, (139,69,19), (self.pos.x+65, self.pos.y), 50)
            pygame.draw.ellipse(screen,(139,69,19), (self.pos.x+45, self.pos.y-65, 40, 60))
            #Face
            pygame.draw.polygon(screen, (218,165,32), ((self.pos.x+55, self.pos.y-45), (self.pos.x+65, self.pos.y-15), (self.pos.x+75, self.pos.y-45)))
            pygame.draw.circle(screen, (255, 255, 255), (self.pos.x+50, self.pos.y-45), 10)
            pygame.draw.circle(screen, (0, 0, 0), (self.pos.x+50, self.pos.y-45), 5)
            pygame.draw.circle(screen, (255, 255, 255), (self.pos.x+80, self.pos.y-45), 10)
            pygame.draw.circle(screen, (0, 0, 0), (self.pos.x+80, self.pos.y-45), 5)



    def move(self):
        if self.num == 0:
            self.pos.y += self.vy
        else:
            self.pos.y += self.vy2
        if self.pos.y >= 800:
            self.pos.y = -100


l = []
for i in range(100):
    l.append(Turkey(rr(0,800), rr(0,800)))


while exit == False:
    clock.tick(60)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    



    screen.fill((0,0,0))
    for i in range(len(l)):
        l[i].move()
        l[i].draw()

    pygame.display.flip()
