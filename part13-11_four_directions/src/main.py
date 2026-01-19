import pygame

pygame.init()
w_w, w_h = 640, 480
window = pygame.display.set_mode((w_w, w_h))

robot = pygame.image.load("robot.png")

x = 0
y = 480  - robot.get_height()
to_left = False
to_right = False
to_top = False
to_bottom = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_top = True
            if event.key == pygame.K_DOWN:
                to_bottom = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_top = False
            if event.key == pygame.K_DOWN:
                to_bottom = False

        if event.type == pygame.QUIT:
            exit()

    if to_right:
        x += 1
    if to_left:
        x -= 1
    if to_top:
        y -= 1
    if to_bottom:
        y += 1
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    clock.tick(60)
