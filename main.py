from config import *

# This is the entrypoint for running the engine. Handles gameloop and initial launch. Gluecode.
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