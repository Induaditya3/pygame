# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint
class V:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @property
    def t(self):
        return (self.x, self.y)

pygame.init()

window = pygame.display.set_mode((640,480))
window_dim = V(*window.get_size())

clock = pygame.time.Clock()
robot= pygame.image.load("robot.png")
speed = 1

def invade(object: pygame.Surface, pos: V):
    object_dim = V(*object.get_size())

    if pos.y > window_dim.y - object_dim.y:
        if pos.x <= window_dim.x/2:
            pos.x -= speed
        else:
            pos.x += speed
    else:
        pos.y += speed

    window.blit(object, pos.t)

invader_list = [(pygame.image.load("robot.png"), V(randint(0,window_dim.x-robot.get_width()),randint(-100,-robot.get_height()))) for _ in range(10)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0,0,0))
    for invader in invader_list:
        if invader[1].x > window_dim.x or invader[1].x < -robot.get_width():
            invader_list.remove(invader)
            invader_list.append((pygame.image.load("robot.png"), V(randint(0,window_dim.x-robot.get_width()),randint(-100,-robot.get_height()))) )
        else:
            invade(*invader)
    pygame.display.flip()

    clock.tick(60)     
