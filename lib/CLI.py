import _queue
import multiprocessing
from cmd import Cmd
from multiprocessing import Process
import GraphicsManager
import pygame


class Console(Cmd):
    prompt = 'dmcli> '
    intro = "Welcome to dmcli!"

    def __init__(self):
        super().__init__()
        self.multiproc_queue = multiprocessing.Queue()
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
        try:
            pygame_state = self.multiproc_queue.get_nowait()
            if pygame_state == "window_quit":
                self.game_window = None
        except _queue.Empty:
            pass

        if self.game_window:
            self.multiproc_queue.put("client_quit")
            pygame.quit()
            self.game_window = None
        else:
            print("Map viewer already closed.")

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
        try:
            pygame_state = self.multiproc_queue.get_nowait()
            if pygame_state == "window_quit":
                self.game_window = None
        except _queue.Empty:
            pass

        if self.game_window is None:
            self.game_window = Process(target=GraphicsManager.GameWindow, args=(self.multiproc_queue,))
            self.game_window.start()
        else:
            print("Map viewer already open.")


    def do_vision(self, arg):
        'help'

    def do_cmd(self, line):
        print(line)

    def do_exit(self, arg):
        print("exiting...")
        if self.game_window:
            self.multiproc_queue.put("client_quit")
            pygame.quit()
            self.game_window = None
        pygame.quit()
        self.game_window = None
        exit()
