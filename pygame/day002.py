# + 간단한 물리(가속도, 마찰력)

import pygame
import sys

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Simple PyGame Example")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

vel_x = 0
vel_y = 0
acceleration = 0.5  # 가속도
friction = 0.9      # 마찰, 속도를 조금씩 줄여주는 효과
max_speed = 5       # 최대 속도
pos_x = 200
pos_y = 200
circle_radius = 20  # 원의 반지름

clock = pygame.time.Clock()

while True:
    vel_x *= friction
    vel_y *= friction
    
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        vel_x -= acceleration
    if key_event[pygame.K_RIGHT]:
        vel_x += acceleration
    if key_event[pygame.K_UP]:
        vel_y -= acceleration
    if key_event[pygame.K_DOWN]:
        vel_y += acceleration

    pos_x += vel_x
    pos_y += vel_y
    
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
