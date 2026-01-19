# WRITE YOUR SOLUTION HERE:
import datetime
import pygame
from math import pi, sin, cos

pygame.init()

window = pygame.display.set_mode((640,480))
w_w, w_h = window.get_size()

clock = pygame.time.Clock()
centre = w_w//2, w_h//2
radius = w_h//2 - 10

second_hand_r = radius * 0.95
minute_hand_r = radius * 0.80
hour_hand_r = radius * 0.70

def end_point(radius: int, time:int, hour:bool = False) -> tuple[int, int]:
    if hour:
        time -= 12
        angle = 2*pi*time/12 - pi/2
    else:
        angle = 2*pi*time/60 - pi/2
    return radius * cos(angle)+ centre[0], radius * sin(angle) + centre[1]

while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            exit(0)

    now = datetime.datetime.now()
    h, m, s = map(int, now.strftime("%H:%M:%S").split(":"))
    pygame.display.set_caption(f"{h}:{m}:{s}")

    
    window.fill((0,0,0))
    pygame.draw.circle(window, (255, 0, 0), centre, radius, 5)
    pygame.draw.circle(window,(255, 0, 0), centre, 10)
    pygame.draw.line(window, (0, 0, 255), centre,end_point(second_hand_r, s))
    pygame.draw.line(window, (0, 0, 255), centre,end_point(minute_hand_r, m), 3)
    pygame.draw.line(window, (0, 0, 255), centre,end_point(hour_hand_r, h, hour=True), 6)
    pygame.display.flip()
    clock.tick(3)
    
