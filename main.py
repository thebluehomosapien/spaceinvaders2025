import pygame, sys
from game import Game
# from spaceship import Spaceship
# # from laser import Laser
# from obstacle import Obstacle

pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700

GREY = (29, 29, 27)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Space Invaders")

clock = pygame.time.Clock()

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)

# spaceship = Spaceship(SCREEN_WIDTH, SCREEN_HEIGHT)
# spaceship_group = pygame.sprite.GroupSingle()
# spaceship_group.add(spaceship)

# obstacle = Obstacle(100, 100)

# laser = Laser((100, 100), 6, SCREEN_HEIGHT)
# laser2 = Laser((100, 200), -6, SCREEN_HEIGHT)
# lasers_group = pygame.sprite.Group()
# lasers_group.add(laser, laser2)

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Updating
    # spaceship_group.update()
    # lasers_group.update()
    game.spaceship_group.update()

    #Drawing
    screen.fill(GREY)
    game.spaceship_group.draw(screen)
    # spaceship_group.draw(screen)
    # lasers_group.draw(screen)
    # spaceship_group.sprite.lasers_group.draw(screen)
    # obstacle.blocks_group.draw(screen)
    game.spaceship_group.sprite.lasers_group.draw(screen)
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)
    game.aliens_group.draw(screen)

    pygame.display.update()
    clock.tick(60)