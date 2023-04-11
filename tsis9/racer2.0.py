import random, pygame

pygame.init()
WIDTH, HEIGHT = 400, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Street Racer v2.0')
background = pygame.image.load("./materials/AnimatedStreet.png")
score_font = pygame.font.SysFont("Verdana", 20)
SCORE = 0
SCORE_COIN = 0

# Класс противник
class Enemy(pygame.sprite.Sprite):
    #Инициализация
    def __init__(self):
        super().__init__()
        self.speed = 0.5
        self.image = pygame.image.load('./materials/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(0, WIDTH - self.rect.width),
            self.rect.height // 2,
        )

    #Отрисовка врага на экране
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    #Обновления данных при выхода за границы экрана
    def update(self):
        global SCORE

        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            SCORE += 1
            self.speed += 0.1
            self.rect.y = 0
            self.rect.x = random.randint(0, WIDTH - self.rect.width)

        if SCORE_COIN > 30:#Увеличение скорости при кол-ве монет > 30
            self.speed += 0.2

#Класс монетка
class Coin(pygame.sprite.Sprite):
    #Инициализация
    def __init__(self):
        super().__init__()
        self.speed = 5
        self.image = pygame.image.load('./materials/imgonline-com-ua-Resize-qGbnIez2QESp.png')
        self.rect = self.image.get_rect()

        self.rect.center = (
            random.randint(0, WIDTH - self.rect.width),
            self.rect.height // 2,
        )

    #Отрисовка монетки на экране
    def draw(self, surface):
        surface.blit(self.image, self.rect)


    #Обновления данных при выходе монетки за границы экранна
    def update(self, group: pygame.sprite.Group):
        global SCORE_COIN

        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            SCORE_COIN += 0
            self.speed += 0.1
            self.rect.y = 0
            self.image.set_alpha(255)
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            if not group.has(self):
                group.add(self)

#Класс игрок
class Player(pygame.sprite.Sprite):
    #Инициализация
    def __init__(self):
        super().__init__()
        self.speed = 15
        self.image = pygame.image.load('./materials/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)

    #Отрисовка игрока на экране
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    #Обновление данных при нажати на кнопки
    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.x >= self.speed:
            self.rect.x -= self.speed
        if pressed[pygame.K_RIGHT] and self.rect.x + self.rect.width + self.speed <= WIDTH:
            self.rect.x += self.speed


def main():
    global SCORE_COIN
    running = True
    player = Player()
    enemy = Enemy()
    coin = Coin()

    enemies = pygame.sprite.Group()
    enemies.add(enemy)

    coins = pygame.sprite.Group()
    coins.add(coin)


    while running:

        SCREEN.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update()
        enemy.update()
        coin.update(coins)

        player.draw(SCREEN)
        enemy.draw(SCREEN)
        coin.draw(SCREEN)

        if pygame.sprite.spritecollideany(player, enemies):
            running = False

        if pygame.sprite.spritecollideany(player, coins):
            SCORE_COIN += random.randint(1, 5)#рандомный номинал монеты
            coin.image.set_alpha(0)
            coin.remove(coins)


        score = score_font.render(f" Your Score: {str(SCORE)}", True, (0, 0, 0))
        score_coin = score_font.render(f" Coins: {str(SCORE_COIN)}", True, (0, 0, 0))
        SCREEN.blit(score, (0, 0))
        SCREEN.blit(score_coin, (290, 0))

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
