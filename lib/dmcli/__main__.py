import sys
from os import path

LIBDIR = path.abspath(path.join(path.dirname(path.abspath(__file__)), path.pardir))
PARDIR = path.abspath(path.join(LIBDIR, path.pardir))

sys.path.append(LIBDIR)
sys.path.append(PARDIR)

from CLI import Console

Console().cmdloop()
p = Console()
p.cmdloop()