import pygame

pygame.init()
screen=pygame.display.set_mode((1000,1000))
done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(400, 300, 200, 200))

    pygame.display.flip()