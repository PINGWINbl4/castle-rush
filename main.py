import pygame
from math import *
window = pygame.display.set_mode((500, 500))


class Rouge:
    # характеристики класса
    def __init__(self):
        mass = 5
        health = 80
        damage = 200
        texture = pygame.draw.rect(window, (255, 255, 255), (20, 20, 20, 20))
        move_speed = 15


class Warrior:
    # характеристики класса
    def __init__(self):
        mass = 15
        health = 150
        damage = 80
        texture = ""
        move_speed = 10
        Fp = mass * 100


class Druid:
    # характеристики класса
    def __init__(self):
        mass = 5
        health = 100
        damage = 50
        texture = ""
        move_speed = 10
        Fp = mass * 100


class Monk:
    # характеристики класса
        move_speed = 30
        mass = 7
        health = 100
        damage1 = 120
        damage2 = 50
        x = 20
        y = 480

        def Move(self, x, y):
            pygame.draw.rect(window, (255, 255, 255), (x, y, 20, 20))


class Ranger:
    # характеристики класса
    move_speed = 15
    mass = 20
    health = 100
    damage1 = 120
    damage2 = 50
    x = 20
    y = 480
    jump_count = 10
    jump = False

    # Осуществление движения
    def Move(self):
        # Захват кнопок и текстурка
        keys = pygame.key.get_pressed()
        pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, 20, 20))

        # проверка нажатия
        if keys[pygame.K_d] and self.x <= 470:
            self.x += self.move_speed
        if keys[pygame.K_a] and self.x >= 10:
            self.x -= self.move_speed
        if keys[pygame.K_w]:
            self.jump = True
        if keys[pygame.K_s] and self.y <= 490:
            self.jump = False
            self.jump_count = 10
            self.y += self.mass

        # прыжок
        if self.jump and self.y<=490:
            if self.jump_count >= -10:
                self.y -= (self.jump_count ** 3) / self.mass
                self.jump_count -= 1
            else:
                self.jump_count = 10
                self.jump = False



pygame.init()
pygame.display.set_caption('castle rush')
player = Ranger

while True:
    window.fill((0, 0, 0))
    player.Move(player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    pygame.display.update()
    pygame.time.delay(25)


