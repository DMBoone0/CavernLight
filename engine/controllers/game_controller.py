"""
Author: Dillon Boone
License: MIT

Primary controller for the flow of the engine. Runs the game loop and orchestrates model and view updates.
"""
from config import *
from input_handler import InputHandler

class GameController:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()
        self.running = True

        self.input_handler = InputHandler()

        self.input_handler.bind_key(KEY_DEFAULTS['sys_menu'], self.quit)
    
    def quit(self):
        self.running = False
        pygame.quit()
        exit()
    
    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            self.screen.fill('black')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            keys = pygame.key.get_pressed()
            self.input_handler.handle_input(keys)