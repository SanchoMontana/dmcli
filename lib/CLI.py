import multiprocessing
import cmd2
import GraphicsManager
from db.DatabaseActions import DB
import pygame
import sys
import inspect
from actions import commands
import readline

from lib.actions import commands

class Console(cmd2.Cmd):
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

    def _cmdloop(self):
        try:
            super()._cmdloop()
        except Exception as e:
            pass

    def preloop(self):
        # Dynamically create commands from actions/commands
        for name in [n for n, _ in inspect.getmembers(commands, inspect.isclass)]:
            if not name.endswith("_Command"):
                continue
            command = getattr(commands, name)
            setattr(Console, 'do_' + command.title, command.do)
            setattr(Console, 'do_' + command.title, cmd2.with_argparser(command.parser)(getattr(Console, "do_" + command.title)))
