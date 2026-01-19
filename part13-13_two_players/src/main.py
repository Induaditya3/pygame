# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
w_w, w_h = 640, 480
window = pygame.display.set_mode((w_w, w_h))

robot = pygame.image.load("robot.png")
robot2 = pygame.image.load("robot.png")

x = 0
y = 480  - robot.get_height()
to_left = False
to_right = False
to_top = False
to_bottom = False

x2 = 0
y2 = 0
to_left2 = False
to_right2 = False
to_top2 = False
to_bottom2 = False

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
                
            if event.key == pygame.K_a:
                to_left2 = True
            if event.key == pygame.K_d:
                to_right2 = True
            if event.key == pygame.K_w:
                to_top2 = True
            if event.key == pygame.K_s:
                to_bottom2 = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_top = False
            if event.key == pygame.K_DOWN:
                to_bottom = False

            if event.key == pygame.K_a:
                to_left2 = False
            if event.key == pygame.K_d:
                to_right2 = False
            if event.key == pygame.K_w:
                to_top2 = False
            if event.key == pygame.K_s:
                to_bottom2 = False
                
        if event.type == pygame.QUIT:
            exit()

    if x+1 < w_w - robot.get_width() and to_right :
        x += 1
    if x-1 > 0 and to_left:
        x -= 1
    if y+1 < w_h - robot.get_height() and to_bottom:
        y += 1
    if y-1 > 0 and to_top:
        y -= 1
        
    if x2+1 < w_w - robot.get_width() and to_right2 :
        x2 += 1
    if x2-1 > 0 and to_left2:
        x2 -= 1
    if y2+1 < w_h - robot.get_height() and to_bottom2:
        y2 += 1
    if y2-1 > 0 and to_top2:
        y2 -= 1
        
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot2, (x2, y2))
    pygame.display.flip()
    clock.tick(60)
