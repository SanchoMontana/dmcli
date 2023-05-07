import os
import sys
from db.DatabaseActions import DB
import shutil

STATEFILE = "collection.state" # FTODO implement state saving



class DMCLI_Manager():
    def __init__(self, dataspace=None):
        self.storage = os.path.join(sys.argv[1], "storage")
        #self.statefile = os.path.join(self.dataspace, STATEFILE)
        self.db = DB(sys.argv[1])
        self.backgrounds = {}
        self.items = {}
        self.monsters = {}
        self.players = {}
        self.characters = {}
        # if os.path.exists(self.statefile):
        #     self.read_state_file()

    def create(self, **kwargs):
        old_filename = kwargs["filename"]
        table_name = kwargs["create"]
        kwargs["filename"] = os.path.join(kwargs["create"], os.path.basename(old_filename))
        shutil.copyfile(old_filename, os.path.join(self.storage, kwargs["filename"]))
        kwargs["name"] = "\"" + kwargs["name"] + "\""
        kwargs["filename"] = "\"" + kwargs["filename"] + "\""
        try:
            del kwargs["cmd2_handler"]
            del kwargs["cmd2_statement"]
            del kwargs["create"]
        except Exception:
            # This is probably alright.
            pass
        self.db.add_table_object(table_name, **kwargs)
