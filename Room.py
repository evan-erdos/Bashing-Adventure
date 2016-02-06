
import yaml
import argparse

from Thing import *

class Room(Thing):
    """
    `Room` : **`Thing`**

    A room is something the player is in.  It has items.
    """

    def __init__(self, args):
        super(self.__class__, self).__init__(args)
        self.args = args

    def Look(args):
        print(self.args[desc])
        return False
