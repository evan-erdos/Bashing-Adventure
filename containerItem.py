
import yaml
import argparse

from item import *

class ContainerItem(Item):
    """
    `ContainerItem` : **`Item`**

    A ContainerItem is an item that can hold other items. Weight/volume limits not implemented.
    """

    def __init__(self, data):
        super(Item, self).__init__(data)

    def putin(args):
        return False

    def takeout(args):
        return False
