'''
1. research on how to render map
2. loading screen
3. sprite of user car / pick car
4. civilian car

https://www.youtube.com/watch?v=IhJCpya_FW8
'''


import pygame
import math
from settings import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GTA original")


background = pygame.image.load("BACKGROUND.jpg").convert()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos = pygame.math.Vector2(PLAYER_START_X, PLAYER_START_Y)
        self.image = pygame.image.load("cars/car(1).png")
        self.size = self.image.get_rect().size
        self.image = pygame.transform.scale(self.image, (int(self.size[1] * PLAYER_SIZE), int(self.size[1])))
        self.rect = self.image.get_rect()
        self.next_y = self.rect.y
        self.next_x = self.rect.x
        self.speed = PLAYER_SPEED


    def user_input(self):
        self.velocity_x = 0
        self.velocity_y = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.velocity_y = -self.speed
        if keys[pygame.K_a]:
            self.velocity_x = -self.speed
        if keys[pygame.K_d]:
            self.velocity_x = self.speed
        if keys[pygame.K_s]:
            self.velocity_y = self.speed

        if self.velocity_x != 0 and self.velocity_y != 0:  # moving diaglonlly
            self.velocity_x /= math.sqrt(2)
            self.velocity_y /= math.sqrt(2)

    def update(self):
        self.user_input()

class Camera (pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.floor_rect = background.get_rect(topleft = (0, 0))

    def custom_draw(self):
        self.offset.x = player.rect.centerx - WIDTH // 2
        self.offset.y = player.rect.centery - HEIGHT // 2

        floor_offset_pos = self.floor_rect.topleft - self.offset
        screen.blit(background, floor_offset_pos)


player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    player_group.update()
    screen.blit(background, (0, 0))
    pygame.display.update()
