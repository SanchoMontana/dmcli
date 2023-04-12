import GraphicsManager
import multiprocessing
import sys
from . import manager
DMCLI_Manager = manager.DMCLI_Manager

class Action_Command:
    title = "action"
    def do(arg):
        pass

class Background_Command:
    title = "background"
    def do(arg):
        pass

class Close_Command:
    title = "close"
    def do(arg):
        "close the pygame instance"
        if GraphicsManager.PYGAME_STATE_TOGGLE.is_set():
            GraphicsManager.PYGAME_STATE_TOGGLE.clear()
        else:
            print("Map viewer already closed.", file=sys.stderr)

class Create_Command:
    title = "create"
    options = ["background", "character", "item", "monster", "player"]
    help = "Creates a [monster, background, item, player, character]."
    def do(arg):
        DMCLI_Manager.create_thing(arg)

class Delete_Command:
    title = "delete"
    def do(arg):
        pass

class Exit_Command:
    title = "exit"
    help = "close dmcli and any existing game window"
    def do(arg):
        print("exiting...")
        GraphicsManager.PYGAME_STATE_TOGGLE.clear()
        exit()

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

class Quit_Command:
    title="quit"
    def do(arg):
        Exit_Command.do(arg)

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
