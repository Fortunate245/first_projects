import sys

import pygame

class Alieninvasion:
    def __init__(self):
        """overall class assets to manage game behaviour"""
        pygame.init()

        self.screen=pygame.display.set_mode((1200.800))

        pygame.display.set_caption("Alien Invasion")

    def run_game(self):

        """Start the main loop for the game"""

        while True:

            for event in event.pygame.get():
                if event.type==pygame.QUIT:
                    sys.exit()

            pygame.display.flip()

if __name__=='__main__':
    ai=Alieninvasion
    ai.run_game()