import _queue
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pyautogui import size as getScreenSize
import multiprocessing
import time
import math


PYGAME_STATE_TOGGLE = multiprocessing.Event()

class GameWindow:
    def __init__(self, pygame_state_toggle):
        self.pygame_state_toggle = pygame_state_toggle
        # Get monitor resolution and set windows dimensions
        self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT = getScreenSize()
        # Window initialization
        pygame.init()
        pygame.mouse.set_visible(False)
        self.game_display = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
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

class DisplayObjects:
    def preview_object(filename, center, zoom, border_color=None):
        # FTODO: make magic numbers... non-magic.
        window_len = 300
        buffer_room = window_len / 15
        center = (zoom * center[0], zoom * center[1])
        cirlce_radius = math.sqrt(2) / 2 * window_len
        cirlce_width = cirlce_radius - (window_len / 2) + buffer_room
        pygame.init()
        game_display = pygame.display.set_mode((window_len, window_len))
        img = pygame.image.load(filename)
        img_size = img.get_size()
        img = pygame.transform.scale_by(img, zoom)
        game_display.blit(img, (window_len / 2 - center[0], window_len / 2 - center[1]))
        pygame.draw.circle(game_display, "black", (window_len / 2, window_len / 2), int(cirlce_radius), width=int(cirlce_width))
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
