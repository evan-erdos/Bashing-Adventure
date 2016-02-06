
import yaml
import argparse

from thing import *

class Room(Thing):
    """
    `Room` : **`Thing`**

    A room is something the player is in.  It has items.
    """

    def __init__(self, data):
        super(self.__class__, self).__init__(data)
        self.data = data

    def Look(args):
        print(self.data[desc])
        return False
