from cmd2 import Cmd2ArgumentParser, Cmd
from . import manager
DMCLI_Manager = manager.DMCLI_Manager()

"""
Class names in this file are very important.
In CLI.py, primary comsole commands are determined by looking at classes in this file that end with "_Command". 
Creating another primary dmcli command, you will ffirst have to create a new class of the form:
class NewCommand_Command:
    title = "newcommand"
    help = "helptext" # FTODO
    def do(arg):
        func = getattr(DMCLI_Manager, Create_Command.title)
        func(namespace)
    parser = CmdArgumentParser()
    ...
"""


class Create_Command:
    title = "create"
    help = "Creates a [monster, background, item, player, character]."
    def do(cmd_obj, namespace):
        func = getattr(DMCLI_Manager, Create_Command.title)
        func(namespace)

    parser = Cmd2ArgumentParser()
    subparser = parser.add_subparsers(dest="create")
    # Creating Groups
    create_background =    subparser.add_parser(name="background")
    create_character =     subparser.add_parser(name="character")
    create_item =          subparser.add_parser(name="item")
    create_monster =       subparser.add_parser(name="monster")
    create_player =        subparser.add_parser(name="player")

    # Background
    create_background.add_argument("name", type=str, help="The name of the background to be submitted.")
    create_background.add_argument("-f", "--filename", completer=Cmd.path_complete, required=True, type=str, help="Filepath of the image to be used as a background")
    create_background.add_argument("-m", "--mode", type=str, choices=["fit", "fill", "stretch"], default="fit",
                            help="Mode of which the background snaps to the dimensions of the screen if the image dimentions do not exactly match the dimentions of the screen")

    # Character
    create_character.add_argument("name", type=str, help="The name of the character to be submitted.")
    create_character.add_argument("-f", "--filename", completer=Cmd.path_complete, required=True, type=str, help="Filename of the image to be used as the character chit.")
    create_character.add_argument("-r", "--radius", type=int, help="Radius of character chit.")
    create_character.add_argument("-x", "--x-center", type=int, help="Location of the desired center of the image (x-axis).")
    create_character.add_argument("-y", "--y-center", type=int, help="Location of the desired center of the image (y-axis).")

    # Item
    create_item.add_argument("name", type=str, help="The name of the item to be submitted.")
    create_item.add_argument("-f", "--filename", completer=Cmd.path_complete, required=True, type=str, help="Filename of the image to be used as the item chit.")
    create_item.add_argument("-r", "--radius", type=int, help="Radius of item chit.")
    create_item.add_argument("-x", "--x-center", type=int, help="Location of the desired center of the image (x-axis).")
    create_item.add_argument("-y", "--y-center", type=int, help="Location of the desired center of the image (y-axis).")
    create_item.add_argument("-d", "--grid-diameter", type=int, help="Diameter of item chit measured in grid units.")

    # Monster
    create_monster.add_argument("name", type=str, help="The name of the monster to be submitted.")
    create_monster.add_argument("-f", "--filename", completer=Cmd.path_complete, required=True, type=str, help="Filename of the image to be used as the monster chit.")
    create_monster.add_argument("-r", "--radius", type=int, help="Radius of monster chit.")
    create_monster.add_argument("-x", "--x-center", type=int, help="Location of the desired center of the image (x-axis).")
    create_monster.add_argument("-y", "--y-center", type=int, help="Location of the desired center of the image (y-axis).")
    create_monster.add_argument("-d", "--grid-diameter", type=int, help="Diameter of item chit measured in grid units.")

    # Player
    create_player.add_argument("name", type=str, help="The name of the player to be submitted.")
    create_player.add_argument("-f", "--filename", completer=Cmd.path_complete, required=True, type=str, help="Filename of the image to be used as the player chit.")
    create_player.add_argument("-r", "--radius", type=int, help="Radius of player chit.")
    create_player.add_argument("-x", "--x-center", type=int, help="Location of the desired center of the image (x-axis).")
    create_player.add_argument("-y", "--y-center", type=int, help="Location of the desired center of the image (y-axis).")


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
"""