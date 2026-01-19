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


def fall(object: pygame.Surface, pos: V):
    global game_over
    if game_over:
        return
    object_dim = V(*object.get_size())
    if pos.y > w_h - object_dim.y:
        game_over = True
    else:
        pos.y += speed
    window.blit(object, pos.t)


def overlaps(object: pygame.Surface, coord: V, object2: pygame.Surface, coord2: V):
    Ax1, Ay1 = coord.t
    Ax2, Ay2 = Ax1 + object.get_width(), Ay1 + object.get_height()

    Bx1, By1 = coord2.t
    Bx2, By2 = Bx1 + object2.get_width(), By1 + object2.get_height()

    return Ax1 <= Bx2 and Bx1 <= Ax2 and Ay1 <= By2 and By1 <= Ay2


pygame.init()
w_w, w_h = 640, 480
window = pygame.display.set_mode((w_w, w_h))
pygame.display.set_caption("Asteroids")
robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")


rock_list = [
    V(randint(0, w_w - rock.get_width()), randint(-400, -5 - rock.get_height()))
    for _ in range(3)
]
x = 0
y = 480 - robot.get_height()
to_left = False
to_right = False
speed = 1
game_over = False
points = 0
point_font = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()

while True:
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False

        if event.type == pygame.QUIT:
            exit()

    if not game_over:
        if x + 1 < w_w - robot.get_width() and to_right:
            x += 5
        if x - 1 > 0 and to_left:
            x -= 5
        for rock_coord in rock_list:
            if overlaps(robot, V(x, y), rock, rock_coord):
                rock_list.remove(rock_coord)
                rock_list.append(
                    V(
                        randint(0, w_w - rock.get_width()),
                        randint(-100, -5 - rock.get_height()),
                    )
                )
                points += 1
                speed = 1 if points//5 == 0 else points//5
            else:
                fall(rock, rock_coord)
    else:
        font = pygame.font.SysFont("Arial", 35, bold=True)
        text = font.render("Game Over!", True, (255, 30, 10))
        window.blit(text, (0.34 * w_w, 0.45 * w_h))

    text = point_font.render(f"Points: {points}", True, (255, 0, 0))
    window.blit(text, (w_w - 120, 3))
    window.blit(robot, (x, y))
    pygame.display.flip()
    clock.tick(60)
