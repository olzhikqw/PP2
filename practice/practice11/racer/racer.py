import pygame, sys
from pygame.locals import *
import random
pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")
font = pygame.font.SysFont("Verdana", 30)
score = 0
coins_collected = 0
coins_for_speed_counter = 0
speed = 5
COINS_FOR_SPEED = 5
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        img = pygame.image.load("images/enemy.png")
        self.image = pygame.transform.smoothscale(img, (90, 140))
        self.rect = self.image.get_rect()
        self.reset()
    def reset(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = 0
    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.top > SCREEN_HEIGHT:
            score += 1
            self.reset()
    def draw(self, surface):
        surface.blit(self.image, self.rect)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        img = pygame.image.load("images/car.png")
        self.image = pygame.transform.smoothscale(img, (90, 140))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 120)
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-7, 0)
        if pressed_keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(7, 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weight = 1
        self.reset()
    def reset(self):
        self.weight = random.choice([1, 2, 3])
        size = 30 + self.weight * 10
        img = pygame.image.load("images/coin.png")
        self.image = pygame.transform.smoothscale(img, (size, size))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-300, -50)
    def move(self):
        self.rect.move_ip(0, speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()
    def draw(self, surface):
        surface.blit(self.image, self.rect)
P1 = Player()
E1 = Enemy()
C1 = Coin()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P1.update()
    E1.move()
    C1.move()
    player_hitbox = P1.rect.inflate(-30, -30)
    enemy_hitbox = E1.rect.inflate(-30, -30)
    coin_hitbox = C1.rect.inflate(-10, -10)
    if player_hitbox.colliderect(enemy_hitbox):
        text = font.render("GAME OVER", True, BLACK)
        rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        DISPLAYSURF.blit(text, rect)
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()
    if player_hitbox.colliderect(coin_hitbox):
        coins_collected += C1.weight
        coins_for_speed_counter += C1.weight
        C1.reset()
        if coins_for_speed_counter >= COINS_FOR_SPEED:
            speed += 1
            coins_for_speed_counter = 0
    DISPLAYSURF.fill((50, 50, 50))
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
    C1.draw(DISPLAYSURF)
    score_text = font.render(f"Score: {score}", True, WHITE)
    DISPLAYSURF.blit(score_text, (20, 20))
    coin_text = font.render(f"Coins: {coins_collected}", True, WHITE)
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 200, 20))
    pygame.display.update()
    FramePerSec.tick(FPS)