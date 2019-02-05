import pygame
from pygame.locals import *
import sys
from Ships.PlayerShips import Ship
import constant
from Shots.ShotFactory import ShotFactory
pygame.init()

# Instanciate other needed classes

shot_factory = ShotFactory()

# Instanciate Pygame stuff

screen = pygame.display.set_mode((1000, 1000))
background = pygame.image.load('Pics/spaceBackground.bmp').convert()
screen.blit(background, (0, 0))

player = Ship.Ship((500, 850), shot_factory)
space_ship_sprites = pygame.sprite.RenderPlain(player)
space_ship_sprites.draw(screen)
pygame.display.update()


clock = pygame.time.Clock()

while True:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                player.move_to_direction(constant.UP)
            if event.key == K_DOWN:
                player.move_to_direction(constant.DOWN)
            if event.key == K_LEFT:
                player.move_to_direction(constant.LEFT)
            if event.key == K_RIGHT:
                player.move_to_direction(constant.RIGHT)
            if event.key == K_f:
                player.activate_shooting()

        elif event.type == KEYUP:
            if event.key == K_UP:
                player.stop_move_to_direction(constant.UP)
            if event.key == K_DOWN:
                player.stop_move_to_direction(constant.DOWN)
            if event.key == K_LEFT:
                player.stop_move_to_direction(constant.LEFT)
            if event.key == K_RIGHT:
                player.stop_move_to_direction(constant.RIGHT)
            if event.key == K_f:
                player.stop_shooting()
    pygame.event.clear()

    screen.blit(background, (0, 0))

    shot_factory.allyShot.update()
    shot_factory.allyShot.draw(screen)
    player.update()
    space_ship_sprites.draw(screen)
    pygame.display.flip()
