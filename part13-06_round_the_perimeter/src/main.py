# WRITE YOUR SOLUTION HERE:


import pygame

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
        return f"({self.x}, {self.y})".x


pygame.init()

window_dim = V(640, 480)
window = pygame.display.set_mode(window_dim.t)

object = pygame.image.load("robot.png")
object_dim = V(*object.get_size())

clock = pygame.time.Clock()

top_left_border = V(0,0)
top_right_border = V(window_dim.x - object_dim.x, 0)
bottom_right_border = V(window_dim.x - object_dim.x, window_dim.y - object_dim.y)
bottom_left_border = V(0, window_dim.y - object_dim.y)

pos = V(0, 0)
speed = 5
velocity = V(speed, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if top_right_border.x < pos.x and velocity.x == speed:
        velocity = V(0, speed)
    elif bottom_right_border.y < pos.y and velocity.y == speed:
        velocity = V(-speed, 0)
    elif pos.x < bottom_left_border.x and velocity.x == -speed:
        velocity = V(0, -speed)
    elif pos.y < top_left_border.y and velocity.y == -speed:
        velocity = V(speed, 0)

    pos = pos + velocity

    window.fill((0,0,0))
    window.blit(object, pos.t)
    pygame.display.flip()
    clock.tick(60)
