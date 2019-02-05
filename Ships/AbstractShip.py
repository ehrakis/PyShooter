import pygame
import constant
from RessourceLoader import load_image
from Shots.ShotFactory import ShotFactory
import math


class AbstractShip(pygame.sprite.Sprite):
    """

    """
    def __init__(self,
                 life_point: int,
                 armor: int,
                 move_speed: int,
                 damage: int,
                 collision_damage: int,
                 canon_number: int,
                 shot_speed: int,
                 reload_time: int,
                 coordinate: tuple,
                 picture: str,
                 vector: tuple,
                 shot_factory: ShotFactory,):
        super(AbstractShip, self).__init__()
        self.life_point = life_point
        self.armor = armor
        self.move_speed = move_speed
        self.damage = damage
        self.collision_damage = collision_damage
        self.canon_number = canon_number
        self.shot_speed = shot_speed
        self.reload_time = reload_time
        self.reloading = 0
        self.image, self.rect = load_image(picture)
        self.rect = self.rect.move_ip(coordinate)
        self.screen = pygame.display.get_surface().get_rect()
        self.shoot = False
        self.shot_factory = shot_factory
        self.vector = vector

    def update(self, *args):

        if len(args) != 0:
            self.rect = self.rect.move_ip(args[0][0], args[0][1])
        else:
            self.rect = self.rect.move((
                self.move_speed / constant.FPS * math.cos(math.atan(self.vector[1]/self.vector[0])),
                self.move_speed / constant.FPS * math.sin(math.atan(self.vector[1]/self.vector[0]))
            ))

        self.shoot_action()

    def shoot_action(self):
        if self.shoot:
            if self.reloading <= 0:
                self.fire()
                self.reloading = self.reload_time
            else:
                self.reloading -= 1

    def activate_shooting(self):
        self.shoot = True

    def stop_shooting(self):
        self.shoot = False

    def fire(self):
        # TODO: transform missile offset by reading datafile
        self.shot_factory.shot((0, -self.shot_speed), self.damage, (self.rect[0] + 21, self.rect[1]), is_ally=True)
        self.shot_factory.shot((0, -self.shot_speed), self.damage, (self.rect[0] + 46, self.rect[1]), is_ally=True)

