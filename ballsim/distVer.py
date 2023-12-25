import pygame
import sys
import os
import time
#initialize pretty much everything
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Josiah's Ball Simulation Recreation")
black = (0, 0, 0)
ball_radius = 20
ball_border_width = 2
ball_speed = [5, 5]
ball_position = [width // 2, height // 2]
speed_increase = 1.1
border_size = 10
border_color = (0, 0, 255)
trail_length = 10
trail = []
color_change_interval = 0.1
last_color_change_time = time.time()
hsv_value = 0
ball_color = pygame.Color(0, 0, 0)
clock = pygame.time.Clock()
os.system("notepad _internal\README.txt" if os.name == 'nt' else "open _internal/README.txt")
def resetSimulation():
    # python gets really confused so....
    global ball_position, ball_speed, trail, screen, width, height
    ball_position = [width // 2, height // 2]
    ball_speed = [5, 5]
    trail = []
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
while True:
    # event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                print("manual reset called")
                resetSimulation()
        elif event.type == pygame.KEYDOWN:
            # this key is probably easy to press accidentally, but meh
            # btw this was added because the window moves constantly and some people don't know of alt f4 lol
            if event.key == pygame.K_BACKSLASH:
                pygame.quit()
                sys.exit()
    try:
        # main loop
        width -= 1
        height -= 1
        screen = pygame.display.set_mode((width, height))
        ball_position[0] += ball_speed[0]
        ball_position[1] += ball_speed[1]
        if ball_position[0] <= ball_radius or ball_position[0] >= width - ball_radius:
            ball_speed[0] = -ball_speed[0] * speed_increase
            if (width < 988):
                width += 30
            if (height < 788):
                height += 30
            screen = pygame.display.set_mode((width, height))
        if ball_position[1] <= ball_radius or ball_position[1] >= height - ball_radius:
            ball_speed[1] = -ball_speed[1] * speed_increase
            if (width < 988):
                width += 30
            if (height < 788):
                height += 30
            screen = pygame.display.set_mode((width, height))
        current_time = time.time()
        if current_time - last_color_change_time >= color_change_interval:
            last_color_change_time = current_time
            hsv_value = (hsv_value + 10) % 360 
            ball_color.hsva = (hsv_value, 100, 100, 100)
        trail.insert(0, (tuple(ball_position), (ball_color.r, ball_color.g, ball_color.b)))
        screen.fill(black)
        for pos, color in trail:
            alpha = 255
            pygame.draw.circle(screen, (0, 0, 0), (int(pos[0]), int(pos[1])), ball_radius + ball_border_width)
            pygame.draw.circle(screen, color, (int(pos[0]), int(pos[1])), ball_radius)
        pygame.draw.circle(screen, (0, 0, 0), (int(ball_position[0]), int(ball_position[1])), ball_radius + ball_border_width)
        pygame.draw.circle(screen, ball_color, (int(ball_position[0]), int(ball_position[1])), ball_radius)
        pygame.draw.rect(screen, border_color, (0, 0, width, border_size))
        pygame.draw.rect(screen, border_color, (0, height - border_size, width, border_size))
        pygame.draw.rect(screen, border_color, (0, 0, border_size, height))
        pygame.draw.rect(screen, border_color, (width - border_size, 0, border_size, height))
        pygame.display.flip()
        clock.tick(60)

    except TypeError:
        # stupid typeerrors
        resetSimulation()
