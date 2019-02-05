from Shots.DifferentShot import AllyShot
import pygame


class ShotFactory:
    """

    """

    def __init__(self):
        self.allyShot = pygame.sprite.Group()
        self.enemyShot = pygame.sprite.Group()

    def shot(self, vector: tuple, damage: int, position: tuple, is_ally=False):
        if is_ally:
            self.allyShot.add(AllyShot.AllyShot(vector, damage, position))

    def update(self):
        self.allyShot.update()

