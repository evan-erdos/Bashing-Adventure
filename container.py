
import yaml
import argparse

from item import *

class Container(Item):
    """
    `Container` : **`Item`**

    A Container is an item that can hold other items. Weight/volume limits not implemented.

    Todo: Description should iterate through contained items.
    """

    def __init__(self, data):
        super(self.__class__, self).__init__(data)

    def putin(args):
        return False

    def takeout(args):
        return False
