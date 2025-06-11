# + 화면 경계 처리

import pygame
import sys

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Simple PyGame Example")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pos_x = 200
pos_y = 200
circle_radius = 20  # 원의 반지름

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        pos_x -= 1
    if key_event[pygame.K_RIGHT]:
        pos_x += 1
    if key_event[pygame.K_UP]:
        pos_y -= 1
    if key_event[pygame.K_DOWN]:
        pos_y += 1

    # 경계 체크: 원이 화면을 넘지 않도록 제한
    if pos_x - circle_radius < 0:
        pos_x = circle_radius  # 왼쪽 경계를 넘지 않도록
    if pos_x + circle_radius > SCREEN_WIDTH:
        pos_x = SCREEN_WIDTH - circle_radius  # 오른쪽 경계를 넘지 않도록
    if pos_y - circle_radius < 0:
        pos_y = circle_radius  # 위쪽 경계를 넘지 않도록
    if pos_y + circle_radius > SCREEN_HEIGHT:
        pos_y = SCREEN_HEIGHT - circle_radius  # 아래쪽 경계를 넘지 않도록

    screen.fill(black)
    pygame.draw.circle(screen, white, (pos_x, pos_y), circle_radius)
    pygame.display.update()
