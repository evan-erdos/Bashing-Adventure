
import yaml
import argparse

from Thing import *

class Item(Thing):
    """
    `Item` : **`Thing`**

    An `Item` is a Thing that can be taken and dropped.
    """

    def __init__(self, arg, desc):
        super(Item, self).__init__(arg, desc)

    def take(args):
        return False

    def drop(args):
        return False
