import pygame

class Obj:
    def __init__(self, bouncing_object):
        self.screen = bouncing_object.screen
        self.settings = bouncing_object.settings
        self.screen_rect = bouncing_object.screen.get_rect()

        self.image = pygame.image.load("img/DVD_logo_green.png")
        self.rect = self.image.get_rect()

    def update(self):
        # update speed if edge reached
        if self.rect.left < 0:
            self.settings.speed[0] = -self.settings.speed[0]
            self.image = pygame.image.load("img/DVD_logo_blue.png")

        if self.rect.right > self.settings.screen_w:
            self.settings.speed[0] = -self.settings.speed[0]
            self.image = pygame.image.load("img/DVD_logo_red.png")

        if self.rect.top < 0:
            self.settings.speed[1] = -self.settings.speed[1]
            self.image = pygame.image.load("img/DVD_logo_green.png")

        if self.rect.bottom > self.settings.screen_h:
            self.settings.speed[1] = -self.settings.speed[1]
            self.image = pygame.image.load("img/DVD_logo_yellow.png")

        # update position
        self.rect.left += self.settings.speed[0]
        self.rect.top += self.settings.speed[1]