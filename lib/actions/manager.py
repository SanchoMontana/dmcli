import os
import sys
from custom_creations.monster import Monster
from db import DatabaseActions
STATEFILE = "collection.state"



class DMCLI_Manager():
  def __init__(self, dataspace=None):
    self.dataspace = os.path.join(sys.__file__, "dataspace")
    self.statefile = None if dataspace is None else os.path.join(self.dataspace, STATEFILE)
    self.backgrounds = {}
    self.items = {}
    self.monsters = {}
    self.players = {}
    self.characters = {}
    if os.path.exists(self.statefile):
      self.read_state_file()

  def update_state_file(self):
    # something to do with pickle
    pass
  
  def read_state_file(self):
    # something to do with pickle
    pass

  def create_thing(self, thing_class, **kwargs):
    print("This is the create_thing method")
    print(thing_class)
    print(kwargs)