import pygame

window = pygame.display.set_mode((1000, 1000))
matrix = [[0 for x in range(1000)] for y in range(1000)]
class Rouge:
    def __init__(self):
        mass = 5
        health = 80
        damage = 200
        texture = pygame.draw.rect(window, (255, 255, 255), (20, 20, 20, 20))
        move_speed = 15
        Fp=mass*100


class Warrior:
    def __init__(self):
        mass = 15
        health = 150
        damage = 80
        texture = ""
        move_speed = 10
        Fp = mass * 100


class Druid:
    def __init__(self):
        mass = 5
        health = 100
        damage = 50
        texture = ""
        move_speed = 10
        Fp = mass * 100

class Monk:
    def __init__(self):
        mass = 8
        health = 120
        damage = 100
        texture = ""
        move_speed = 20
        Fp = mass * 100

class Ranger:
    def __init__(self):
        mass = 7
        health = 100
        damage1 = 120
        damage2 = 50
        texture = ""
        move_speed = 15

    def Move(self,x,y, move_speed):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= move_speed
        if keys[pygame.K_RIGHT] and x < 24:
            x += move_speed
        if keys[pygame.K_UP] and y > 0:
            y -= move_speed
        if keys[pygame.K_DOWN] and y < 24:
            y += move_speed


pygame.init()
pygame.display.set_caption('castle rush')

while True:
    player = Rouge
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    keys = pygame.key.get_pressed()


