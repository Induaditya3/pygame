# WRITE YOUR SOLUTION HERE:
import pygame


class V:
    def __init__(self, x: float, y: float):
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

window = pygame.display.set_mode((640,480))
window_dim = V(*window.get_size())

clock = pygame.time.Clock()

ball = pygame.image.load("ball.png")
ball_radius = ball.get_width()

pos = V(300,200)
velocity = V(1,3)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0,0,0))
    window.blit(ball, pos.t)
    pos = pos + velocity
    pygame.display.flip()

    if pos.y >= window_dim.y- ball_radius or pos.y <= 0:
        velocity = V(velocity.x, -velocity.y)
    elif pos.x >= window_dim.x - ball_radius or pos.x <= 0:
        velocity = V(-velocity.x, velocity.y)
    clock.tick(60)     
