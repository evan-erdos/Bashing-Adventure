
import yaml
import argparse

from thing import *

class Item(Thing):
    """
    `Item` : **`Thing`**

    An `Item` is a Thing that can be taken and dropped.
    """

    def __init__(self, data):
        super(Item, self).__init__(data)

    def take(args):
        return False

    def drop(args):
        return False
