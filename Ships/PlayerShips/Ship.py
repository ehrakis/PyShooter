import pygame
import constant
import math
from RessourceLoader import load_image
from Shots.ShotFactory import ShotFactory


class Ship(pygame.sprite.Sprite):
    """
    Represent the player in-game as a space ship.
    """
    def __init__(self, coordinate: tuple, shot_factory: ShotFactory):
        super(Ship, self).__init__()
        self.life_point = 100
        self.reload_time = 8
        self.shot_speed = 15
        self.damage = 50
        self.armor = 0
        self.shield = 0
        self.move_speed = 400
        self.image, self.rect = load_image("spaceship.bmp")
        self.movement = {
            "UP": (0, -1),
            "DOWN": (0, 1),
            "RIGHT": (1, 0),
            "LEFT": (-1, 0)
        }
        self.action = set()
        self.screen = pygame.display.get_surface().get_rect()
        self.rect.move_ip(coordinate)
        self.shoot = False
        self.shot_factory = shot_factory
        self.reloading = 0

    def update(self, *args):
        action_number = self.action.__len__()
        for action in self.action:
            if action_number >= 2:
                movement = [round(value * (math.cos(math.pi/4)) * (self.move_speed / constant.FPS)) for value in action]
            else:
                movement = [round(value * (self.move_speed/constant.FPS))for value in action]

            new_position = self.rect.move((movement[0], movement[1]))
            if self.screen.contains(new_position):
                self.rect = new_position

        if self.shoot:
            if self.reloading <= 0:
                self.fire()
                self.reloading = self.reload_time
            else:
                self.reloading -= 1
        pygame.event.pump()

    def move_to_direction(self, direction):
        self.action.add(self.movement[direction])
        pygame.event.pump()

    def stop_move_to_direction(self, direction):
        if self.movement[direction] in self.action:
            self.action.remove(self.movement[direction])

    def activate_shooting(self):
        self.shoot = True

    def stop_shooting(self):
        self.shoot = False

    def fire(self):
        self.shot_factory.shot((0, -self.shot_speed), self.damage, (self.rect[0] + 21, self.rect[1]), is_ally=True)
        self.shot_factory.shot((0, -self.shot_speed), self.damage, (self.rect[0] + 46, self.rect[1]), is_ally=True)

