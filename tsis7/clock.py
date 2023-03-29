import pygame
from datetime import datetime
import math

RES = WIDTH, HEIGHT = 1000, 750
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
RADIUS = H_HEIGHT - 50
radius_list = {'sec': RADIUS - 100, 'min': RADIUS - 200}

pygame.init()
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()


cl60 = dict(zip(range(60), range(0, 360, 6)))

img = pygame.image.load('img/mickeyclock3.jpeg').convert_alpha()


def get_clock_pos(clock_dict, clock_hand, key):
    x = H_WIDTH + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_HEIGHT + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    t = datetime.now()
    minute, second = t.minute % 60, t.second

    screen.blit(img, (0, 0))

    pygame.draw.line(screen, pygame.Color('black'), (H_WIDTH, H_HEIGHT), get_clock_pos(cl60, minute, 'min'), 10)
    pygame.draw.line(screen, pygame.Color('black'), (H_WIDTH, H_HEIGHT), get_clock_pos(cl60, second, 'sec'), 5)

    pygame.display.flip()
    clock.tick(20)
