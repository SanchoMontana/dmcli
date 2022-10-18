from cmd import Cmd
import threading
import GraphicsManager
import pygame

class Guess():
    def __init__(self):
        self.red = "Red"
    def go(self):
        pass


class Console(Cmd):
    prompt = 'dmcli> '
    intro = "Welcome to dmcli!"

    def __init__(self):
        super().__init__()
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
        pygame.quite()
        self.game_window = None

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

    def do_start(self, arg):
        'help'
        if self.game_window is None:
            self.game_window = GraphicsManager.GameWindow()

    def do_vision(self, arg):
        'help'

    def do_cmd(self, line):
        print(line)

    def do_exit(self, arg):
        print("exiting...")
        pygame.quit()
        self.game_window = None
        return True

if __name__ == '__main__':
    Console().cmdloop()
    p = Console()
    p.cmdloop()
