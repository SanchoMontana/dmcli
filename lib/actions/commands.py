from . import parsers
import GraphicsManager
import multiprocessing
import sys


class Action_Command:
    title = "action"
    def run_command(arg):
        "help"
        pass

class Background_Command:
    title = "background"
    def run_command(arg):
        "help"
        pass

class Close_Command:
    title = "close"
    def run_command(arg):
        "close the pygame instance"
        if GraphicsManager.PYGAME_STATE_TOGGLE.is_set():
            GraphicsManager.PYGAME_STATE_TOGGLE.clear()
        else:
            print("Map viewer already closed.", file=sys.stderr)

class Create_Command:
    title = "create"
    def run_command(arg):
        arg = parsers.Create_parser.parse(arg)
        print(vars(arg))

class Delete_Command:
    title = "delete"
    def run_command(arg):
        "help"
        pass

class Exit_Command:
    title = "exit"
    def run_command(arg):
        "close dmcli and any existing game window"
        print("exiting...")
        GraphicsManager.PYGAME_STATE_TOGGLE.clear()
        exit()

class Grid_Command:
    title = "grid"
    def run_command(arg):
        "help"
        pass

class Health_Command:
    title = "health"
    def run_command(arg):
        "help"
        pass

class Initiative_Command:
    title = "initiative"
    def run_command(arg):
        "help"
        pass

class Move_Command:
    title = "move"
    def run_command(arg):
        "help"
        pass

class Ping_Command:
    title = "ping"
    def run_command(arg):
        "help"
        pass

class Quit_Command:
    title="quit"
    def run_command(arg):
        Exit_Command.run_command(arg)

class Start_Command:
    title = "start"
    def run_command(arg):
        "instatiate a pygame instance"
        if not GraphicsManager.PYGAME_STATE_TOGGLE.is_set():
            game_window = multiprocessing.Process(target=GraphicsManager.GameWindow, args=(GraphicsManager.PYGAME_STATE_TOGGLE,))
            game_window.start()
            GraphicsManager.PYGAME_STATE_TOGGLE.set()
        else:
            print("Map viewer already open.", file=sys.stderr)

class Vision_Command:
    title = "vision"
    def run_command(arg):
        "help"
        pass
