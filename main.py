import pygame, sys
from spaceship import Spaceship
# from laser import Laser

pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700

GREY = (29, 29, 27)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Space Invaders")

clock = pygame.time.Clock()

spaceship = Spaceship(SCREEN_WIDTH, SCREEN_HEIGHT)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

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
    spaceship_group.update()
    # lasers_group.update()

    #Drawing
    screen.fill(GREY)
    spaceship_group.draw(screen)
    # lasers_group.draw(screen)
    spaceship_group.sprite.lasers_group.draw(screen)

    pygame.display.update()
    clock.tick(60)