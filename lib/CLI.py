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
            # setattr(self, 'complete_' + command.title, self.completecmd)

    # def completecmd(self, text, line, beginning_index, ending_index):
    #     words = line.split(" ")
    #     for name in [n for n, _ in inspect.getmembers(commands, inspect.isclass)]:
    #         if not name.endswith("_Command"):
    #             continue
    #         if words[0] == name.split('_')[0].lower():
    #             command_class = getattr(commands, name)
    #             options = command_class.options
    #             return options
    #     return options
