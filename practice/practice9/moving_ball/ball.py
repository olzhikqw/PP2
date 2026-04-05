import pygame
x,y=300, 200
radius=25
speed=5
w,h=600,400
def move(keys):
    global x, y
    if keys[pygame.K_LEFT] and x-radius-speed>=0:
        x-=speed
    if keys[pygame.K_RIGHT] and x+radius+speed<=w:
        x+=speed
    if keys[pygame.K_UP] and y-radius-speed>=0:
        y-=speed
    if keys[pygame.K_DOWN] and y+radius+speed<=h:
        y+=speed
def draw(screen):
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)