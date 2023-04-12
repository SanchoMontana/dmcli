import multiprocessing
from cmd import Cmd
import GraphicsManager
from db.DatabaseActions import DB
import pygame
import sys
import inspect
from actions import commands
import readline



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
        # This completion logic is just for the first word in each command.
        # This is so flippin pythonic...
        all_commands = [n.split("_", 1)[0].lower() for n, _ in inspect.getmembers(commands, inspect.isclass) if n.endswith("_Command")]
        options = [a for a in all_commands if a.startswith(text)]
        if len(options) == 1:
            if text == options[0]:
                readline.insert_text(" ")
                return []
            else:
                options[0] += " "
        return options
    
    def completedefault(self, text, line, begidx, endidx):
        """Method called to complete an input line when no command-specific
        complete_*() method is available.
        """
        cmd_class = None
        all_options = []
        smart_options = []
        if len(line.split(" ")) == 2:
            base_cmd = line.split(" ")[0]
            for n, _ in inspect.getmembers(commands, inspect.isclass):
                cmd, ending = n.split('_', 1) # TODO: This may throw an error if there is a class in commands.py that doens't have an underscore in the name.
                if cmd.lower().startswith(base_cmd) and ending == "Command":
                    cmd_class = getattr(commands, n)
            if cmd_class:
                if hasattr(cmd_class, "options"):
                    all_options = cmd_class.options
            if all_options:
                for i in all_options:
                    if i.startswith(text):
                        smart_options.append(i)
                if len(smart_options) == 1:
                    if text.split(" ", 1)[0] == smart_options[0]:
                        # if tab completed when the arg is already complete.
                        readline.insert_text(" ")
                        return []
                    else:
                        smart_options[0] += " "
        return smart_options
