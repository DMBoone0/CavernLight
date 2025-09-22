#!/usr/bin/env python

"""
Author: Dillon Boone
License: MIT

Entrypoint to the 'engine' if that is what this is. Primary nexus of the glue code.
Primary role is just startup and running the game loop. All logic is deferred to other modules.
"""

from config import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()
        self.running = True
    
    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            self.screen.fill('black')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

if __name__ == '__main__':
    game = Game()
    game.run()