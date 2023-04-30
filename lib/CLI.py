import multiprocessing
from cmd2 import Cmd
import GraphicsManager
from db.DatabaseActions import DB
import pygame
import sys
import inspect
from actions import commands, command_args
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
            setattr(self, 'do_' + command.title, command.do)
    
    def do_quit(self):
        super().do_quit(self)

    # def do_exit(self):
    #     print("exiting...")
    #     GraphicsManager.PYGAME_STATE_TOGGLE.clear()
    #     self.do_quit()
        
    def completenames(self, text, *ignored):
        # This completion logic is just for the first word in each command.
        # This is so flippin pythonic...
        all_commands = [n.split("_", 1)[0].lower() for n, _ in inspect.getmembers(commands, inspect.isclass) if n.endswith("_Command")]
        options = [a for a in all_commands if a.startswith(text)]
        if len(options) == 1:
            if text == options[0]:
                # if tab completed when the arg is already complete.
                readline.insert_text(" ")
                return []
            else:
                options[0] += " "
        return options
    
    def completedefault(self, text, line, begidx, endidx):
        c = []
        parser = command_args.universal_parser
        command_map = self.get_arg_map(parser)
        """
        # Get rid of excess spaces that people will inevitably add
        new_line = " ".join(line.split())
        new_begidx = begidx
        new_endidx = endidx
        previous_space = line.startswith(" ")
        for i in range(len(line)):
            if line[i] == " ":
                if previous_space:
                    if i < begidx:
                        new_begidx -= 1
                    if i < endidx:
                        new_endidx -= 1
                else:
                    previous_space = True
        line = new_line
        begidx = new_begidx
        endidx = new_endidx
        """
        # Weird edge case where cmd does not pick up if tabbed text is '-' or '--'
        if begidx == endidx:
            while line[:begidx].endswith('-'):
                begidx -= 1
                text = '-' + text
        
        tokens = line.split()
        tmp = line[:endidx]
        tabbed_word_index = len(tmp.split()) - 1
        tabbed_flag = None
        for token in tmp.split()[::-1]:
            if token.startswith("-"):
                tabbed_flag = token
                break

        token_dict = command_map
        used_flags = []
        all_flags = []
        positionals = 0
        for token in tokens:
            if token in token_dict.keys() and token not in ["positionals", "flags"]:
                token_dict = token_dict[token]
            else:
                if "positionals" in token_dict.keys() and "flags" in token_dict.keys():
                    if positionals != len(token_dict["positionals"]):
                        identifier = token_dict["positionals"][positionals]
                        positionals += 1
                    else:
                        all_flags = token_dict["flags"]
                        for option_strings in token_dict["flags"]:
                            if token in option_strings:
                                used_flags.append(option_strings)

        if "positionals" in token_dict.keys():
            if positionals != len(token_dict["positionals"]):
                return []
        if "flags" in token_dict.keys():
            if text.startswith('-'):
                for flag in all_flags:
                    if flag not in used_flags:
                        c += [i for i in flag if i.startswith(text)]
            # Filesystem checks
            else:
                if tabbed_flag in ["-f", "--filename"]: # This flag is of course reserved for, well... filenames.
                    c += self.path_complete(text, line, begidx, endidx)
        else:
            for k in token_dict.keys():
                if k.startswith(text):
                    c += [k]
        
        return c

    def get_arg_map(self, parser):
        arg_map = {}
        if hasattr(parser, "_actions"):
            for action in parser._actions:
                if action.dest != "help":
                    if hasattr(action, "_actions") or (hasattr(action, "choices") and action.choices and type(action.choices) != list):
                        arg_map[action.dest] = self.get_arg_map(action)
                    else:
                        if "positionals" not in arg_map.keys():
                            arg_map["positionals"] = []
                            arg_map["flags"] = []
                        if not action.option_strings:
                            arg_map["positionals"].append(action.dest)
                        else:
                            arg_map["flags"].append(action.option_strings)
        elif hasattr(parser, "choices") and parser.choices != None:
            if type(parser.choices) == list:
                arg_map[parser.dest] = []
                for choice in parser.choices:
                    arg_map[parser.dest].append(choice)
            else:
                for choice, choice_parser in parser.choices.items():
                    arg_map[choice] = self.get_arg_map(choice_parser)
        else:
            return action.dest
        return arg_map