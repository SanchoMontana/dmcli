import pygame
from pyautogui import size as getScreenSize

class GameWindow():
    def __init__(self):
        self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT = getScreenSize()
        # Get monitor resolution and set windows dimensions
        # Window initialization
        pygame.init()
        pygame.mouse.set_visible(False)
        self.gameDisplay = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        self.clock = pygame.time.Clock()
        self.FPS = 1
        self.game_exit = False

    def quit(self):
        pygame.quit()
        return


