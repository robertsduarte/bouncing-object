import pygame
import sys
from settings import Settings
from obj import Obj

class BouncingObject:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
                (self.settings.screen_w, self.settings.screen_h))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Bouncing Object Animation")
        self.obj = Obj(self)

    def run_animation(self):
        while True:
            self._check_events()
            self.obj.update()
            self._update_screen()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_colour)
        self.screen.blit(self.obj.image, self.obj.rect)
        pygame.display.flip()
        self.clock.tick(self.settings.fps)


if __name__ == '__main__':
    animation1 = BouncingObject()
    animation1.run_animation()
