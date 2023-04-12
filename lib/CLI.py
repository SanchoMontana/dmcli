import multiprocessing
from cmd import Cmd
import GraphicsManager
from db.DatabaseActions import DB
import pygame
import sys
import inspect
from actions import commands



class Console(Cmd):
    prompt = '(dmcli) '
    intro = "Welcome to dmcli!"
    def __init__(self, working_dir):
        super().__init__()
        self.pygame_state_toggle = multiprocessing.Event()
        self.DB = DB(working_dir)
        self.monsters = []
        self.pcs = []
        self.npcs = []
        self.items = []

    def preloop(self):
        # Dynamically create commands from actions/commands
        for name in [n for n, _ in inspect.getmembers(commands, inspect.isclass)]:
            if not name.endswith("_Command"):
                continue
            command = getattr(commands, name)
            setattr(self, 'do_' + command.title, command.do)

    def completenames(self, text, *ignored):
        # This is so flippin pythonic...
        all_commands = [n.split("_", 1)[0].lower() for n, _ in inspect.getmembers(commands, inspect.isclass) if n.endswith("_Command")]
        return [a for a in all_commands if a.startswith(text)]
