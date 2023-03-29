import pygame

s_width = 400
s_height = 400

white = (255, 255, 255)
red = (255, 0, 0)

step = 20

ball_radius = 25
ball_x = (s_width - ball_radius) // 2
ball_y = (s_height - ball_radius) // 2


pygame.init()

screen = pygame.display.set_mode((s_width, s_height))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y = max(ball_y - step, ball_radius)
            elif event.key == pygame.K_DOWN:
                ball_y = min(ball_y + step, s_height - ball_radius)
            elif event.key == pygame.K_LEFT:
                ball_x = max(ball_x - step, ball_radius)
            elif event.key == pygame.K_RIGHT:
                ball_x = min(ball_x + step, s_width - ball_radius)

    screen.fill(white)

    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)

    pygame.display.flip()


