import argparse


class Create_parser:
    def parse(line):
        parser = argparse.ArgumentParser(
                    prog='create',
                    description='Creates an object of type [BACKGROUND, CHARACTER, ITEM, MONSTER, PLAYER]')
        parser.add_argument('object_type', choices=["background", "character", "item", "monster", "player"])
        args = parser.parse_args(args=line.split())
        return args