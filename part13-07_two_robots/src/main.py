# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
window_dim = window.get_size()

robot = pygame.image.load("robot.png")
robot2 = pygame.image.load("robot.png")

clock = pygame.time.Clock()

def bounce_horizontal(object: pygame.Surface, speed: int, pos: tuple[int, int]):
    object_dim = object.get_size()

    pos = (pos[0]+speed, pos[1])
    if pos[0] >= window_dim[0]-object_dim[0] and speed > 0:
        speed = -speed
    elif pos[0] <= 0 and speed <= 0:
        speed = -speed

    window.blit(object, pos)
    return pos, speed


pos1 = (0,0)
pos2 = (0,robot.get_height()+10)
speed = 4
speed2 = speed*2
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    window.fill((0, 0, 0))
    pos1, speed  = bounce_horizontal(robot,speed, pos1)
    pos2, speed2 = bounce_horizontal(robot2,speed2, pos2)

    pygame.display.flip()
    clock.tick(60)
