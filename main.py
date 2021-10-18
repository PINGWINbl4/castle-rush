import pygame
import time
window = pygame.display.set_mode((500, 500))
timer = pygame.time.Clock()
timer.tick(60)

class Ranger:
    # характеристики класса
    move_speed = 15
    mass = 20
    health = 100
    damage1 = 120
    damage2 = 50
    x = 20
    y = 450
    jump_count = 10
    jump = False

    # Осуществление движения
    def Move(self):
        # Захват кнопок и текстурка
        keys = pygame.key.get_pressed()
        pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, 30, 30))
        # проверка нажатия
        if keys[pygame.K_d] and self.x <= 460:
            self.x += self.move_speed

        elif keys[pygame.K_a] and self.x >= 10:
            self.x -= self.move_speed

        elif keys[pygame.K_w]:
            self.jump = True

        elif keys[pygame.K_s]:
            while self.y<450:
                self.jump = False
                self.jump_count = 10
                self.y += self.mass

            # прыжок
        if self.jump:
            if self.jump_count >= -10:
                self.y -= (self.jump_count ** 3) / self.mass
                self.jump_count -= 1
            else:
                self.jump_count = 10
                self.jump = False

        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if keys[pygame.K_e]:
                    self.x += self.move_speed * 10
                    if self.x > 470:
                        self.x = 470

                if keys[pygame.K_q]:
                    self.x -= self.move_speed * 10
                    if self.x < 0:
                        self.x = 0

            elif event.type == pygame.QUIT:
                exit()

        if self.y > 450:
            self.y = 450


pygame.init()
pygame.display.set_caption('castle rush')
player = Ranger

while True:

    window.fill((0, 0, 0))
    player.Move(player)

    pygame.display.update()
    pygame.time.delay(20)


