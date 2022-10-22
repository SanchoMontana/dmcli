import _queue
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pyautogui import size as getScreenSize


class GameWindow:
    def __init__(self, multiproc_queue):
        self.multiproc_queue = multiproc_queue
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
        while not self.game_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.game_exit = True
                    self.multiproc_queue.put("window_quit")
            try:
                if self.multiproc_queue.get_nowait() == "client_quit":
                    pygame.quit()
                    self.game_exit = True
            except _queue.Empty:
                pass
            self.clock.tick(self.FPS)
        return
