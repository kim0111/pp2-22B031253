import random
import time
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 800
BLACK = (0, 0, 0)
GRID = (69, 123, 0)
RED = (255, 0, 0)
BODY = (6, 79, 0)
YELLOW = (255, 255, 0)
GRASS = (69, 163, 0)
WHITE = (255, 255, 255)
font = pygame.font.SysFont(None, 40)


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BLOCK_SIZE = 40

pygame.display.set_caption('Snake v2.0')
score_font = pygame.font.SysFont("Verdana", 20)




#Класс кординат
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Food:
    #Инициализация
    def __init__(self, x, y):
        self.location = Point(x, y)
        self.food_time_created = time.time()
        self.time_limit = 5.5

    #Кордината X
    @property
    def x(self):
        return self.location.x

    #Кордината Y
    @property
    def y(self):
        return self.location.y

    #Рисует на экране еду для змейки
    def update(self):
        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )

    #создание новой еды(создание кординат для еды и
    def new_food(self):
        self.location = Point(random.randint(0, WIDTH // BLOCK_SIZE - 1), random.randint(0, HEIGHT // BLOCK_SIZE - 1))
        self.food_time_created = time.time()

    #метод который показывает истекло ли время еды
    def is_food_expired(self):
        if time.time() - self.food_time_created > self.time_limit:
            return True
        return False



class Bomb:
    def __init__(self, x, y):
        self.location = Point(x, y)

    @property
    def x(self):
        return self.location.x

    @property
    def y(self):
        return self.location.y

    def update(self):
        pygame.draw.rect(
            SCREEN,
            BLACK,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )


#ласс змейки
class Snake:
    #Инициализация
    def __init__(self):
        self.points = [
            Point(WIDTH // BLOCK_SIZE // 2, HEIGHT // BLOCK_SIZE // 2),
            Point(WIDTH // BLOCK_SIZE // 2 + 1, HEIGHT // BLOCK_SIZE // 2),
        ]

    #Рисует тело и голову змейки
    def update(self):
        head = self.points[0]

        pygame.draw.rect(
            SCREEN,
            YELLOW,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.points[1:]:
            pygame.draw.rect(
                SCREEN,
                BODY,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

    #основной метод который отвичает за движение змейки
    def move(self, dx, dy):
        for idx in range(len(self.points) - 1, 0, -1):
            self.points[idx].x = self.points[idx - 1].x
            self.points[idx].y = self.points[idx - 1].y

        self.points[0].x += dx
        self.points[0].y += dy

        head = self.points[0]
        if head.x > WIDTH // BLOCK_SIZE:
            head.x = 0
        elif head.x < 0:
            head.x = WIDTH // BLOCK_SIZE - 1
        elif head.y > HEIGHT // BLOCK_SIZE:
            head.y = 0
        elif head.y < 0:
            head.y = HEIGHT // BLOCK_SIZE - 1

    #метод проверяет сталкивается ли голова змеи с едой
    def check_collision(self, food):
        if self.points[0].x != food.x:
            return False
        if self.points[0].y != food.y:
            return False
        return True

    def check_collision_bomb(self, bomb):
        if self.points[0].x != bomb.x:
            return False
        if self.points[0].y != bomb.y:
            return False
        return True

#Отрисовка сетки поля
def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, GRID, (x, 0), (x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, GRID, (0, y), (WIDTH, y), width=1)

def draw_end():
    win_text = "Game is over!"
    win_img = font.render(win_text, True, WHITE)
    pygame.draw.rect(SCREEN, RED, (WIDTH // 2 - 100, HEIGHT // 2 - 20, 200, 50))
    SCREEN.blit(win_img, (WIDTH // 2 - 100, HEIGHT // 2 - 10))



def main():
    running = True
    snake = Snake()
    food = Food(5, 5)
    bomb = Bomb(10, 10)
    dx, dy = 0, 0
    foods_eaten = 0
    speed = 3
    level = 3

    while running:
        SCREEN.fill(GRASS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, +1
                elif event.key == pygame.K_LEFT:
                    dx, dy = -1, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = +1, 0

        score = score_font.render(f"Level:{str(level)}", True, (255, 0, 0))
        SCREEN.blit(score, (5, 0))

        snake.move(dx, dy)
        if snake.check_collision(food):
            snake.points.append(Point(food.x, food.y))
            food.new_food()
            foods_eaten += random.randint(1, 2)
            if foods_eaten >= 1 or foods_eaten <= 5:
                speed += 0.1
                level += foods_eaten
                foods_eaten = 0

        if snake.check_collision_bomb(bomb):
            snake.points.pop()
            level -= 2
            bomb.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            bomb.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)

        if len(snake.points) == 0 or level <= 0:
            draw_end()
            pygame.display.update()
            time.sleep(1)
            break

        if food.is_food_expired():
            food.new_food()

        food.update()
        bomb.update()
        snake.update()
        draw_grid()

        pygame.display.flip()
        clock.tick(speed)


if __name__ == '__main__':
    main()

