import pygame

pygame.init()
pygame.font.init()

health_font = pygame.font.SysFont('OCR A Extended', 15)
stamina_font = pygame.font.SysFont('OCR A Extended', 10)


class Ranger(pygame.sprite.Sprite):
    # характеристики класса
    move_speed = 15
    mass = 20
    health = 100.0
    stamina = 100.0
    damage1 = 120
    damage2 = 50
    x = 20
    y = 450
    jump_count = 10
    jump = False

    def __init__(self, x, y, file_name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file_name).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

    # Осуществление движения
    def Move(self):
        # Захват кнопок и текстурка
        keys = pygame.key.get_pressed()
        main_char = Ranger(self.x, self.y, 'ranger.png')
        window.blit(main_char.image, main_char.rect)
        if self.x<5:
            self.x = 5
        if self.x>465:
            self.x = 465

        if self.stamina<100:
            self.stamina += 0.5
        # проверка нажатия
        if keys[pygame.K_d]:
            self.x += self.move_speed

        elif keys[pygame.K_a]:
            self.x -= self.move_speed

        elif keys[pygame.K_w]:
            self.jump = True

        elif keys[pygame.K_LEFT]:
            pygame.draw.rect(window,(255, 0, 0),(self.x + 30, self.y + 15, 50, 3))


            # прыжок
        if self.jump:
            if self.stamina <10:
                self.jump = False
            else:
                if self.jump_count >= -10:
                    self.y -= (self.jump_count ** 3) / self.mass
                    self.jump_count -= 1
                else:
                    self.stamina -= 10
                    self.jump_count = 10
                    self.jump = False

        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if keys[pygame.K_e]:
                    if self.stamina > 40:
                        self.stamina -= 40
                        self.x += self.move_speed * 10

                if keys[pygame.K_q]:
                    if self.stamina >40:
                        self.stamina -= 40
                        self.x -= self.move_speed * 10

                if keys[pygame.K_s]:
                    if self.stamina >= 15:
                        self.stamina -= 15
                        while self.y < 450:
                            self.jump = False
                            self.jump_count = 10
                            self.y += self.mass
                    else:
                        pass

            elif event.type == pygame.QUIT:
                exit()

        if self.y > 450:
            self.y = 450
        pygame.draw.rect(window, (64, 0, 0), (5, 10, 120, 25))
        pygame.draw.rect(window, (255, 0, 0), (5, 10, self.health*1.5, 25))
        pygame.draw.rect(window,(0, 64, 0),(5, 40, 100, 15))
        pygame.draw.rect(window,(0, 255, 0),(5, 40, self.stamina,15))
        window.blit((health_font.render(f"{self.health}", 1, (0, 0, 0), (255, 0, 0))),(5,12))
        window.blit((stamina_font.render(f"{self.stamina}", 1, (0, 0, 0), (0, 255, 0))),(5,40))



class_list = [Ranger]
window = pygame.display.set_mode((500, 500))
timer = pygame.time.Clock()
timer.tick(200)
keys = pygame.key.get_pressed()



pygame.display.set_caption('castle rush')
player = Ranger

# основная игра
while True:

    window.fill((0, 0, 0))
    player.Move(player)
    pygame.font.init()
    pygame.display.update()
    pygame.time.delay(20)
