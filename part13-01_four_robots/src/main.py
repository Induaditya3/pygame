
# The exercises in this part of the course have no automated tests, as the results as visually verified.
# The tests grant points automatically as you submit your solution to the server, no matter what your implementation.
# Only submit your solution when you are ready, and your solution matches the exercise description.
# The exercises may not have automatic tests, but the course staff will still see your solution.
# If your solution clearly does not match the exercise description, you may lose the points granted for the exercises in this part.

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

    @property
    def t(self):
        return (self.x, self.y)
    
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    
import pygame

pygame.init()

window_dim = V(640, 480)
window = pygame.display.set_mode(window_dim.t)

robot = pygame.image.load("robot.png")
robot_dim = V(robot.get_width(), robot.get_height())

window.fill((0, 0, 0))

top_left = V(0, 0)
top_right = V(window_dim.x - robot_dim.x, 0)
bottom_left = V(0, window_dim.y - robot_dim.y)
bottom_right = window_dim - robot_dim

window.blit(robot, top_left.t)
window.blit(robot, top_right.t)
window.blit(robot, bottom_left.t)
window.blit(robot, bottom_right.t)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
