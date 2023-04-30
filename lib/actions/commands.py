import GraphicsManager
import multiprocessing
import sys
from . import manager
DMCLI_Manager = manager.DMCLI_Manager()

"""
Class names in this file are very important.
In CLI.py, primary comsole commands are determined by looking at classes in this file that end with "_Command". 
Creating another primary dmcli command, you will ffirst have to create a new class of the form:
class NewCommand_Command:
    title = "newcommand"
    options = [<list of secondary commands>] # See Create_Command class for example usage
    help = "helptext" # FTODO
    def do(arg):
        ... # Internal logic

"""


class Action_Command:
    title = "action"
    def do(arg):
        pass

class Background_Command:
    title = "background"
    def do(arg):
        pass

class Close_Command:
    # FTODO: save statefile
    title = "close"
    def do(arg):
        "close the pygame instance"
        if GraphicsManager.PYGAME_STATE_TOGGLE.is_set():
            GraphicsManager.PYGAME_STATE_TOGGLE.clear()
        else:
            print("Map viewer already closed.", file=sys.stderr)

class Create_Command:
    title = "create"
    help = "Creates a [monster, background, item, player, character]."
    def do(arg):
        DMCLI_Manager.create(arg)

class Delete_Command:
    title = "delete"
    def do(arg):
        pass

class Grid_Command:
    title = "grid"
    def do(arg):
        pass

class Health_Command:
    title = "health"
    def do(arg):
        pass

class Initiative_Command:
    title = "initiative"
    def do(arg):
        pass

class Move_Command:
    title = "move"
    def do(arg):
        pass

class Ping_Command:
    title = "ping"
    def do(arg):
        pass


class Start_Command:
    title = "start"
    def do(arg):
        "instatiate a pygame instance"
        if not GraphicsManager.PYGAME_STATE_TOGGLE.is_set():
            game_window = multiprocessing.Process(target=GraphicsManager.GameWindow, args=(GraphicsManager.PYGAME_STATE_TOGGLE,))
            game_window.start()
            GraphicsManager.PYGAME_STATE_TOGGLE.set()
        else:
            print("Map viewer already open.", file=sys.stderr)

class Vision_Command:
    title = "vision"
    def do(arg):
        pass


# TODO: Maybe create a player command to manage leveling up characters, health adjustments... Either only things in the DB or all things including movement etc.
