"""
Name of the program: Teleporter Game
@author            : Induaditya3
Built using        : pygame 2.6.1 (SDL 2.28.4, Python 3.11.14)
Code formatter     : ruff 0.14.11
Published on       : January 19, 2026
"""
# robot:
#      the robot is the playable character
#      it can move up, down, left and right using arrow keys
#      players point will increase as the robot collects the coins
#
# the other elements of the game are:
#
# gate:
#      if robot comes in contact with gate, it is transported to random location on the screen and control is reversed
#      i.e. left becomes right and up becomes down and vice versa.
#      also, the coins start rising up or fall from above. in other words, direction of the coin is reversed
#
# monster:
#      if robot touches monster then the health of the robot is decreased by 1
#      the robot has total of 3 health points

import pygame
from random import randrange


class Teleporter:
    def __init__(self):
        pygame.init()

        self.load_images()

        self.game_font = pygame.font.SysFont("Arial", 24)

        self.height = 14
        self.width = 24
        self.scale = self.images["coin"].get_height()

        self.window_height = self.scale * self.height
        self.window_width = self.scale * self.width
        self.window = pygame.display.set_mode(
            (self.window_width, self.window_height + self.scale)
        )

        pygame.display.set_caption("Teleporter")
        self.clock = pygame.time.Clock()

        self.left_pressed, self.right_pressed, self.up_pressed, self.down_pressed = (
            False,
            False,
            False,
            False,
        )
        self.new_game()
        self.main_loop()

    def load_images(self):
        files = ["coin", "door", "monster", "robot"]
        self.images = {file: pygame.image.load(file + ".png") for file in files}

    # following series of methods that starts with new_<object> return random coordinates of the object along with speed
    # as per the rules defined in the update method
    # also door speed is same self.speed so its only coordinates is computed 
    def new_coin_fall(self):
        return (
            randrange(self.speed, self.speed + 3),
            randrange(
                0, self.window_width - self.images["coin"].get_width(), self.space
            ),
            randrange(-500, -self.images["coin"].get_height(), self.space),
        )

    def new_coin_rise(self):
        return (
            randrange(self.speed, self.speed + 3),
            randrange(
                0, self.window_width - self.images["coin"].get_width(), self.space
            ),
            randrange(self.window_height, self.window_height + 500, self.space),
        )

    def new_monster_left(self):
        return (
            randrange(self.speed, self.speed + 4),
            randrange(self.window_width, self.window_width + 500, self.space),
            randrange(
                0,
                self.window_height - self.images["monster"].get_height(),
                self.space,
            ),
        )

    def new_monster_right(self):
        return (
            randrange(self.speed, self.speed + 4),
            randrange(-500, -self.images["monster"].get_width(), self.space),
            randrange(
                0,
                self.window_height - self.images["monster"].get_height(),
                self.space,
            ),
        )

    def new_door_left(self):
        return (
            randrange(self.window_width, self.window_width + 100, self.space),
            randrange(
                0, self.window_height - self.images["door"].get_height(), self.space
            ),
        )

    def new_door_right(self):
        return (
            randrange(-100, -self.images["door"].get_width(), self.space),
            randrange(
                0, self.window_height - self.images["door"].get_height(), self.space
            ),
        )

    def new_robot(self):
        return (
            randrange(0, self.window_width - self.images["robot"].get_width()),
            randrange(0, self.window_height - self.images["robot"].get_height()),
        )

    # checks if two suface came in contact or not
    @staticmethod
    def overlaps(
        object: pygame.Surface,
        coord: tuple[int, int],
        object2: pygame.Surface,
        coord2: tuple[int, int],
    ):
        Ax1, Ay1 = coord
        Ax2, Ay2 = Ax1 + object.get_width(), Ay1 + object.get_height()

        Bx1, By1 = coord2
        Bx2, By2 = Bx1 + object2.get_width(), By1 + object2.get_height()

        return Ax1 <= Bx2 and Bx1 <= Ax2 and Ay1 <= By2 and By1 <= Ay2

    def move_robot(self):
        # amount by which to increment robot's position
        step = 5
        # update robot coordinates based on key press and self.fall
        # left movement
        if (
            (self.left_pressed and self.fall) or (self.right_pressed and not self.fall)
        ) and self.robot_x - step > 0:
            self.robot_x -= step
        # right movement
        elif (
            (self.right_pressed and self.fall) or (self.left_pressed and not self.fall)
        ) and self.robot_x + step < self.window_width - self.images[
            "robot"
        ].get_width():
            self.robot_x += step
        # up movement
        elif (
            (self.up_pressed and self.fall) or (self.down_pressed and not self.fall)
        ) and self.robot_y - step > 0:
            self.robot_y -= step
        # down movement
        elif (
            (self.down_pressed and self.fall) or (self.up_pressed and not self.fall)
        ) and self.robot_y + step < self.window_height - self.images[
            "robot"
        ].get_height():
            self.robot_y += step

        robot_coord = self.robot_x, self.robot_y
        # check hit by monster
        monsters_coord = self.monsters_left if self.fall else self.monsters_right
        for coord in monsters_coord:
            if self.overlaps(
                self.images["robot"], robot_coord, self.images["monster"], (coord[1], coord[2])
            ):
                self.lives -= 1
                if self.lives < 0:
                    self.game_over = True
                    return
                else:
                    # since robot struck monster, remove that monster's coordinate and spawn a new one
                    self.monsters_left.remove(
                        coord
                    ) if self.fall else self.monsters_right.remove(coord)
                    self.monsters_left.append(
                        self.new_monster_left()
                    ) if self.fall else self.monsters_right.append(
                        self.new_monster_right()
                    )
        # check hit by coins
        coins_coord = self.coins_fall if self.fall else self.coins_rise
        for coord in coins_coord:
            if self.overlaps(
                self.images["robot"], robot_coord, self.images["coin"], (coord[1], coord[2])
            ):
                self.points += 1
                # remove collected coin and spawn new one
                self.coins_fall.remove(coord) if self.fall else self.coins_rise.remove(
                    coord
                )
                self.coins_fall.append(
                    self.new_coin_fall()
                ) if self.fall else self.coins_rise.append(self.new_coin_rise())
        # check hit by door
        door_coord = (
            (self.door_left_x, self.door_left_y)
            if self.fall
            else (self.door_right_x, self.door_right_y)
        )
        if self.overlaps(
            self.images["robot"], robot_coord, self.images["door"], door_coord
        ):
            # when robot hit by door, we rotate robot 180 degrees and change objects' direction
            self.fall = not self.fall
            self.images["robot"] = pygame.transform.rotate(self.images["robot"], 180)
            self.robot_x, self.robot_y = self.new_robot()

    def new_game(self):
        # minimum spacing between objects
        self.space = self.images["monster"].get_width()
        # base speed
        self.speed = 1
        self.game_over = False
        # determines whether coin fall or rises / arrow key behavior is reversed or not
        self.fall = True

        # initial lives of the player
        self.lives = 3

        # no of coins collected
        self.points = 0

        # reset the orientation of the robot from previous game
        self.images["robot"] = pygame.image.load("robot.png")
        # initial pos of robot
        self.robot_x = randrange(
            0, self.window_width - self.images["robot"].get_width(), self.space
        )
        self.robot_y = self.window_height - self.images["robot"].get_height()

        # when self.fall is true, falling list of coins will be updated
        # this list stores the speed and coordinates
        # x varies from left to right most of visible range of window
        # y varies from -500 to height of coin, so that initially coins are above the visible range of window
        self.coins_fall = [self.new_coin_fall() for _ in range(10)]
        # when self.fall is false, rising list of coins will be updated
        # similary this will  store speed and coordinates
        # x varies form left to right most visible range of window
        # y varies from self.window_height to below the visible range of window
        self.coins_rise = [self.new_coin_rise() for _ in range(10)]

        # when self.fall is true, monster appear from right and move toward left
        self.monsters_left = [self.new_monster_left() for _ in range(10)]
        # when self.fall is false, monster appear from left and move toward right
        self.monsters_right = [self.new_monster_right() for _ in range(10)]

        # intial pos of doors
        # it moves from right to left
        self.door_left_x, self.door_left_y = self.new_door_left()
        # it moves toward right
        self.door_right_x, self.door_right_y = self.new_door_right()

    def update(self):
        if not self.game_over:
            self.move_robot()
            # base speed
            # monster's speed = base speed to  base speed + 4
            # coin's speed = base speed to  base speed + 3
            # door's speed = base speed + 5
            self.speed = 1 if self.points // 10 == 0 else self.points // 10
            # this will update coordinates of all objects except the robot
            if self.fall:
                self.coins_fall = [
                    self.new_coin_fall()
                    if y - self.images["coin"].get_height() > self.window_height
                    else (speed, x, y + speed + 2)
                    for speed, x, y in self.coins_fall
                ]
                self.monsters_left = [
                    self.new_monster_left()
                    if x + self.images["monster"].get_width() < 0
                    else (speed, x - speed, y)
                    for  speed, x, y in self.monsters_left
                ]
                self.door_left_x, self.door_left_y = (
                    (self.door_left_x - self.speed - 5, self.door_left_y)
                    if self.door_left_x + self.images["door"].get_width() > 0
                    else self.new_door_left()
                )
            else:
                self.coins_rise = [
                    self.new_coin_rise()
                    if y + self.images["coin"].get_height() < 0
                    else (speed, x, y - speed - 2)
                    for  speed, x, y in self.coins_rise
                ]
                self.monsters_right = [
                    self.new_monster_right()
                    if x > self.window_width
                    else (speed, x + speed, y)
                    for speed, x, y in self.monsters_right
                ]
                self.door_right_x, self.door_right_y = (
                    self.new_door_right()
                    if self.door_right_x > self.window_width
                    else (self.door_right_x + self.speed + 5, self.door_right_y)
                )

    def main_loop(self):
        while True:
            self.check_events()
            self.update()
            self.draw_window()
            self.clock.tick(30)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.left_pressed = True
                if event.key == pygame.K_RIGHT:
                    self.right_pressed = True
                if event.key == pygame.K_UP:
                    self.up_pressed = True
                if event.key == pygame.K_DOWN:
                    self.down_pressed = True
                if event.key == pygame.K_F2:
                    self.new_game()
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.left_pressed = False
                if event.key == pygame.K_RIGHT:
                    self.right_pressed = False
                if event.key == pygame.K_UP:
                    self.up_pressed = False
                if event.key == pygame.K_DOWN:
                    self.down_pressed = False
            if event.type == pygame.QUIT:
                exit()

    def draw_objects(self):
        self.window.blit(self.images["robot"], (self.robot_x, self.robot_y))

        if self.fall:
            coin_coord = self.coins_fall
            # objects that moves toward left
            monster_coord = self.monsters_left
            door_coord = self.door_left_x, self.door_left_y
        else:
            coin_coord = self.coins_rise
            # objects that move toward right
            monster_coord = self.monsters_right
            door_coord = self.door_right_x, self.door_right_y

        # draw all the objects
        for _, *coord in monster_coord:
            self.window.blit(self.images["monster"], coord)

        for _, *coord in coin_coord:
            self.window.blit(self.images["coin"], coord)

        self.window.blit(self.images["door"], door_coord)

    def draw_window(self):
        self.window.fill((10, 10, 10))

        pygame.draw.rect(
            self.window,
            (49, 47, 47),
            (0, self.window_height, self.window_width, self.scale),
        )

        game_text = self.game_font.render(
            f"Lives left: {0 if self.lives < 0 else self.lives}", True, (103, 154, 175)
        )
        self.window.blit(game_text, (25, self.height * self.scale + 10))

        game_text = self.game_font.render("F2 = New game", True, (255, 255, 255))
        self.window.blit(game_text, (200, self.height * self.scale + 10))

        game_text = self.game_font.render("Esc = Exit game", True, (255, 0, 0))
        self.window.blit(game_text, (400, self.height * self.scale + 10))

        game_text = self.game_font.render(
            f"Points: {self.points}", True, (69, 122, 145)
        )
        self.window.blit(game_text, (self.window_width - 120, 3))
        self.draw_objects()
        if self.game_over:
            font = pygame.font.SysFont("Arial", 36, True)
            game_text = font.render("Game Over!", True, (255, 0, 0))
            game_text_x = self.scale * self.width / 2 - game_text.get_width() / 2
            game_text_y = self.scale * self.height / 2 - game_text.get_height() / 2
            self.window.blit(game_text, (game_text_x, game_text_y))

        pygame.display.flip()


if __name__ == "__main__":
    Teleporter()
