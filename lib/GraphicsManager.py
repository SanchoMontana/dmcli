import _queue
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pyautogui import size as getScreenSize
import multiprocessing

PYGAME_STATE_TOGGLE = multiprocessing.Event()

class GameWindow:
    def __init__(self, pygame_state_toggle):
        self.pygame_state_toggle = pygame_state_toggle
        # Get monitor resolution and set windows dimensions
        self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT = getScreenSize()
        # Window initialization
        pygame.init()
        pygame.mouse.set_visible(False)
        self.gameDisplay = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        self.clock = pygame.time.Clock()
        self.FPS = 5
        self.game_exit = False
        self.run()

    def run(self):
        while self.pygame_state_toggle.is_set():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.pygame_state_toggle.set()
                    self.pygame_state_toggle.set()
            self.clock.tick(self.FPS)
        pygame.quit()
        return
