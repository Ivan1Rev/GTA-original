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
black = (0, 0, 0)
background = pygame.image.load("BACKGROUND.jpg").convert()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos = pygame.math.Vector2(PLAYER_START_X, PLAYER_START_Y)
        self.original_image = pygame.image.load("cars/car(1).png")
        self.size = self.original_image.get_rect().size
        self.original_image = pygame.transform.scale(self.original_image, (int(self.size[1] * PLAYER_SIZE), int(self.size[1])))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(self.pos.x, self.pos.y))
        self.angle = 0
        self.speed = PLAYER_SPEED
        self.velocity_x = 0
        self.velocity_y = 0

    def user_input(self):
        keys = pygame.key.get_pressed()

        # Rotation
        if keys[pygame.K_d]:
            self.angle -= PLAYER_ROTATION_SPEED
        if keys[pygame.K_a]:
            self.angle += PLAYER_ROTATION_SPEED

        # Calculate direction vector
        direction = pygame.math.Vector2(0, -1).rotate(-self.angle)

        # Movement
        self.velocity_x = 0
        self.velocity_y = 0
        if keys[pygame.K_w]:
            self.velocity_x = direction.x * self.speed
            self.velocity_y = direction.y * self.speed
        if keys[pygame.K_s]:
            self.velocity_x = -direction.x * self.speed
            self.velocity_y = -direction.y * self.speed

    def update(self):
        self.user_input()

        # Rotate the image
        self.image = pygame.transform.rotate(self.original_image, self.angle-PLAYER_ROT)
        self.rect = self.image.get_rect(center=self.rect.center)

        # Update position based on velocity
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.floor_rect = background.get_rect(topleft=(0, 0))

    def custom_draw(self):
        self.offset.x = player.rect.centerx - WIDTH // 2
        self.offset.y = player.rect.centery - HEIGHT // 2

        floor_offset_pos = self.floor_rect.topleft - self.offset
        screen.blit(background, floor_offset_pos)

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

while True:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    player_group.update()

    screen.blit(background, (0, 0))
    player_group.draw(screen)
    pygame.display.update()
