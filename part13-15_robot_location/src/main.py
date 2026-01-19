# WRITE YOUR SOLUTION HERE:
from random import randint
import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))
w_w, w_h = window.get_size()
robot = pygame.image.load("robot.png")
r_w, r_h = robot.get_size()

def clicked_on_object(object: pygame.Surface, object_pos: tuple[int, int],  mouse_pos: tuple[int, int]):
    object_dim  = object.get_size()
    if object_pos[0] <= mouse_pos[0] <= object_pos[0] + object_dim[0] and object_pos[1] <= mouse_pos[1] <= object_pos[1] + object_dim[1]:
        return True
    return False
 
clock = pygame.time.Clock()

x, y = randint(0, w_w- r_w), randint(0, w_h-r_h)
window.fill((0, 0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if clicked_on_object(robot,(x, y), event.pos):
                x, y = randint(0, w_w- r_w), randint(0, w_h-r_h)
        if event.type == pygame.QUIT:
            exit(0)

    window.fill((0,0,0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)
