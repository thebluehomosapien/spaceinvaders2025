import pygame, sys, random
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

SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer(SHOOT_LASER, 300)

MYSTERYSHIP = pygame.USEREVENT + 1
pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))
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
        if event.type == SHOOT_LASER:
            game.alien_shoot_laser()
        
        if event.type == MYSTERYSHIP:
            game.create_mystery_ship()
            pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))
    #Updating
    # spaceship_group.update()
    # lasers_group.update()
    game.spaceship_group.update()
    game.move_aliens()
    game.alien_lasers_group.update()
    game.mystery_ship_group.update()
    game.check_for_collisions()
    

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
    game.alien_lasers_group.draw(screen)
    game.mystery_ship_group.draw(screen)

    pygame.display.update()
    clock.tick(60)