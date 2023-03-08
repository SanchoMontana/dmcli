import multiprocessing
from cmd import Cmd
import GraphicsManager
import pygame
import sys


class Console(Cmd):
    prompt = 'dmcli> '
    intro = "Welcome to dmcli!"

    def __init__(self):
        super().__init__()
        self.pygame_state_toggle = multiprocessing.Event()
        self.game_window = None
        self.game_thread = None
        self.monsters = []
        self.pcs = []
        self.npcs = []
        self.items = []

    def do_action(self, line):
        'help'

    def do_background(self, arg):
        'help'

    def do_create(self, arg):
        'help'

    def do_close(self, arg):
        'help'
        if self.pygame_state_toggle.is_set():
            self.pygame_state_toggle.clear()
            self.game_window.join()
        else:
            print("Map viewer already closed.", file=sys.stderr)

    def do_delete(self, arg):
        'help'

    def do_grid(self, arg):
        'help'

    def do_health(self, arg):
        'help'

    def do_initiative(self, arg):
        'help'

    def do_move(self, arg):
        'help'

    def do_ping(self, arg):
        'help'

    def do_quit(self, arg):
        'help'
        self.do_exit(arg)

    def do_start(self, arg):
        'help'
        if not self.pygame_state_toggle.is_set():
            self.game_window = multiprocessing.Process(target=GraphicsManager.GameWindow, args=(self.pygame_state_toggle,))
            self.game_window.start()
            self.pygame_state_toggle.set()
        else:
            print("Map viewer already open.", file=sys.stderr)


    def do_vision(self, arg):
        'help'

    def do_cmd(self, line):
        print(line)

    def do_exit(self, arg):
        print("exiting...")
        if self.game_window:
            self.pygame_state_toggle.clear()
            self.game_window.join()
            pygame.quit() # TODO: do i need this
            self.game_window = None
        pygame.quit() # TODO: do i need this
        self.game_window = None
        exit()
