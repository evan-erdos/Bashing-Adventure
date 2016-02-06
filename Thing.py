
import yaml
import argparse


class Thing:
    """
    `Thing` : **`object`**

    A `Thing` is the lowest common denominator of game entities,
    and describes anything which can be seen or manifested in-game.
    """

    def __init__(self, arg, desc):
        self.arg = arg
        self.desc = desc


    def look(args):
        print(self.desc)
        return False
