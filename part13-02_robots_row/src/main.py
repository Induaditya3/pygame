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
        return V(self.x/const, self.y/const)
    
    @property
    def t(self):
        return (self.x, self.y)
    
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    
import pygame

def row(n: int, initial_pad_y: int, object: pygame.Surface):
    object_dim = V(object.get_width(), object.get_height())
    
    # no of available row for drawing object
    actual_n = window_dim.x / object_dim.x

    if actual_n < n:
        print("no space available for given no of object")
        print(f"so drawing {actual_n-1} no of objects")

        # resetting n
        n = actual_n - 1

    # initial left padding
    initial_pad_x = (actual_n - n)* object_dim.x / 2
    
    # coordinates of objects
    coordinates = [(initial_pad_x + i * object_dim.x, initial_pad_y) for i in range(n)]

    draw_objects(object, coordinates)
        
def draw_objects(object: pygame.Surface, coordinates: list[tuple[int, int]]):
    for cordinate in coordinates:
        window.blit(object, cordinate)


pygame.init()

window_dim = V(640, 480)
window = pygame.display.set_mode(window_dim.t)

robot = pygame.image.load("robot.png")
robot_dim = V(robot.get_width(), robot.get_height())

window.fill((0, 0, 0))

row(10, 100, robot)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
