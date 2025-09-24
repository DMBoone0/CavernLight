"""
Author: Dillon Boone
License: MIT

Primary controller for the flow of the engine. Runs the game loop and orchestrates model and view updates.
"""
import pygame
from config import *
from .command_dispatcher import CommandDispatcher, CommandType
from game.scenes import DungeonScene

class GameController:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()
        self.running = True

        self.dispatcher = CommandDispatcher()
        self.dispatcher.bind_key(pygame.K_w, CommandType.MOVE_FORWARD)
        self.dispatcher.bind_key(pygame.K_s, CommandType.MOVE_BACKWARD)
        self.dispatcher.bind_key(pygame.K_a, CommandType.TURN_LEFT)
        self.dispatcher.bind_key(pygame.K_d, CommandType.TURN_RIGHT)

        self.scene = DungeonScene()
    
    def quit(self):
        self.running = False
        pygame.quit()
        exit()
    
    def run(self):
        # Draw/Render loop
        while self.running:
            dt = self.clock.tick() / 1000
            self.screen.fill('black')

            # Event loop
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    pygame.quit()
                    exit()
                else:
                    command = self.dispatcher.dispatch(event)
                    if command:
                        self.scene.handle_command(command)