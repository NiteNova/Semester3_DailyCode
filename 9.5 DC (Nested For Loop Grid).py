import pygame
pygame.init()
pygame.display.set_caption("Graphical for loops")
screen = pygame.display.set_mode((800, 800))

while(1):


    for i in range (10):
        for k in range(10):
            pygame.draw.rect(screen, (200, 0, 100), (i*100, k*100, 100, 100), 1)


    pygame.display.flip()

pygame.quit
