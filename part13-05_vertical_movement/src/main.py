# WRITE YOUR SOLUTION HERE:

class V:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self,other: "V"):
        return V(self.x+other.x, self.y+other.y)
    
    def __sub__(self, other: "V"):
        return V(self.x - other.x, self.y - other.y)
    
    def __mul__(self, const: float):
        return V(self.x* const, self.y * const)
    
    __rmul__ = __mul__

    def __truediv__(self, const: float):
        return V(round(self.x/const), round(self.y/const))
    
    @property
    def t(self):
        return (self.x, self.y)
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

from math import sin, cos    
import pygame

pygame.init()

window_dim = V(640, 480)
window = pygame.display.set_mode(window_dim.t)

robot = pygame.image.load("robot.png")

robot_dim = V(robot.get_width(), robot.get_height())

clock = pygame.time.Clock()

pos = V(0, 0)
velocity = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0,0,0))

    if pos.y + robot_dim.y > window_dim.y and velocity > 0:
        velocity = -1
    elif pos.y < 0 and velocity < 0:
        velocity = 1

    pos.y = pos.y + velocity
    
    # print(pos)
    window.blit(robot, pos.t)
    pygame.display.flip()


    clock.tick(60)
