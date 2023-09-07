import pygame
pygame.init()
pygame.display.set_caption("Graphical For Loop")
screen = pygame.display.set_mode((800, 800))

gameover = False

while not gameover:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

    for i in range (1, 9):
       for g in range (1, 9):
          pygame.draw.rect(screen, (200, 0, 100), (85*i, 90*g, 30, 30))
          pygame.draw.rect(screen, (70, 0, 150), (85*i+5, 90*g+4, 20.8, 20.8))
          
    for i in range (1, 8):
        for g in range (1,8):
          pygame.draw.rect(screen, (0, 50, 100), (85*i+42, 90*g+42, 30, 30))
          pygame.draw.rect(screen, (0, 0, 0), (85*i+42+5, 90*g+42+4, 20.8, 20.8))

    pygame.display.flip()

pygame.quit()
