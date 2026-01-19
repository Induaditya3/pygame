# WRITE YOUR SOLUTION HERE:
import pygame
from math import sin, cos, pi

pygame.init()

window = pygame.display.set_mode((640, 480))
window_dim = window.get_size()

def rotate_object(objects: list[pygame.Surface], angles: list[int], radius):
    def draw_object(object: pygame.Surface, angle: int, radius: int):
        # find the x, y coordinate given angle
        x = window_dim[0]/2 + cos(angle)*radius - object.get_width()/2
        y = window_dim[1]/2 + sin(angle)*radius - object.get_height()/2
        window.blit(object,(x,y))

    for object, angle in zip(objects,angles):
        draw_object(object, angle, radius)

angles = [angle*2*pi/10 for angle in range(10)]
robots = [pygame.image.load("robot.png") for _ in range(10)]

window.fill((0,0,0))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    rotate_object(robots, angles, 100)
    pygame.display.flip()
    # update all angles by 0.01 radians
    angles = [angle + 0.01 for angle in angles]
    clock.tick(60)
    
