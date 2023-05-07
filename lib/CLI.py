import multiprocessing
import cmd2
import GraphicsManager
import pygame
import sys
import inspect
from actions import commands
import readline

from lib.actions import commands

class Console(cmd2.Cmd):
    prompt = '(dmcli) '
    intro = "Welcome to dmcli!"
    def __init__(self):
        super().__init__(allow_cli_args=False)
        self.pygame_state_toggle = multiprocessing.Event()

    def preloop(self):
        # Dynamically create commands from actions/commands
        for name in [n for n, _ in inspect.getmembers(commands, inspect.isclass)]:
            if not name.endswith("_Command"):
                continue
            command = getattr(commands, name)
            setattr(Console, 'do_' + command.title, command.do)
            setattr(Console, 'do_' + command.title, cmd2.with_argparser(command.parser)(getattr(Console, "do_" + command.title)))
