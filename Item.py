
import yaml
import argparse


class Item(Thing):
	"""
	`Item` : **`Thing`**

	An `Item` is a Thing that can be taken and dropped.
	"""

        def __init__(self, arg):
                super(Item, self).__init__(arg)

        def take(args):
                return False

        def drop(args):
                return False
