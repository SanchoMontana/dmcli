import os
import sys
from db import DatabaseActions
import shutil

STATEFILE = "collection.state" # FTODO implement state saving



class DMCLI_Manager():
    def __init__(self, dataspace=None):
        self.dataspace = os.path.join(sys.path[0], "dataspace")
        self.statefile = os.path.join(self.dataspace, STATEFILE)
        self.db = os.path.join(sys.path[0], "storage", "sqlite3.db")
        self.backgrounds = {}
        self.items = {}
        self.monsters = {}
        self.players = {}
        self.characters = {}
        if os.path.exists(self.statefile):
            self.read_state_file()

    def create(self, namespace):
        getattr(self, "create_" + namespace.create)(namespace)
  
    def create_background(self, namespace):
        pass

    def create_character(self, namespace):
        pass

    def create_item(self, namespace):
        pass

    def create_monster(self, namespace):
        pass

    def create_player(self, namespace):
        pass