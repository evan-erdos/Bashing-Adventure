
import yaml
import argparse

from Thing import *

class Room(Thing):
    """
    `Room` : **`Thing`**

    A room is something the player is in.  It has items.
    """

    def __init__(self, arg, desc):
        super(self.__class__, self).__init__(arg, desc)
        self.arg = arg


    def Look(args):
        print(desc)
        return False
