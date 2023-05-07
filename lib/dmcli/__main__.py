import sys
import os

LIBDIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir))
PARDIR = os.path.abspath(os.path.join(LIBDIR, os.path.pardir))

sys.path.append(LIBDIR)
sys.path.append(PARDIR)

from db import DataStore
db = DataStore.DataStore(sys.argv[1])

from CLI import Console
p = Console()
p.cmdloop()
exit()