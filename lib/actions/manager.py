import os
import sys
from .command_args import *
#from db import DatabaseActions
import shlex

STATEFILE = "collection.state" # FTODO implement state saving



class DMCLI_Manager():
  def __init__(self, dataspace=None):
    self.dataspace = os.path.join(sys.path[0], "dataspace")
    self.statefile = os.path.join(self.dataspace, STATEFILE)
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

  def create(self, line):
    pass