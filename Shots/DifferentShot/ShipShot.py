import pygame
from RessourceLoader import load_image


class ShipShot(pygame.sprite.Sprite):
    """
    Abstract class that represent a ship's shot
    """

    def __init__(self, vector: tuple, damage: int, position: tuple, image: str):
        super(ShipShot, self).__init__()
        self.vector = vector
        self.damage = damage
        self.image, self.rect = load_image(image)
        self.rect.move_ip(position)
        self.screen = pygame.display.get_surface().get_rect()

    def update(self, *args):
        new_position = self.rect = self.rect.move(self.vector)
        if self.screen.contains(new_position):
            self.rect = new_position
        else:
            self.kill()
