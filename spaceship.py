import pygame

class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\Users\gamer\Desktop\spaceinvaders2025\graphics\spaceship.png")