import os
import sys
from db.DatabaseActions import DB
import shutil 
from GraphicsManager import GameWindow, DisplayObjects

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
        if kwargs["preview"]:
            DisplayObjects.preview_object(kwargs["filename"], (kwargs["x_center"], kwargs["y_center"]), kwargs["zoom"])
            return
        old_filename = kwargs["filename"]
        table_name = kwargs["create"]
        kwargs["filename"] = os.path.join(kwargs["create"], os.path.basename(old_filename))
        # FTODO: Use OpenCV or Pillow to crop and dilate (if necessary) the image... Ideally image would be a png in the shape of a circle --> then save the edited version of the picture in the storage filesystem.
        # FTODO: Add timestamp or something to outgoing filename to guarantee uniqueness.
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
