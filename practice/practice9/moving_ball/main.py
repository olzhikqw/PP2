import pygame
from ball import move, draw
pygame.init()
screen=pygame.display.set_mode((600, 400))
clock=pygame.time.Clock()
r=True
while r:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            r=False
    keys=pygame.key.get_pressed()
    move(keys)
    draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()