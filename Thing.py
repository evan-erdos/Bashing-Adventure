import yaml
import argparse


class Thing:
	"""
	`Thing` : **`object`**

	A `Thing` is the lowest common denominator of game entities,
	and describes anything which can be seen or manifested in-game.
	"""

	description = "You're in a room!"


	def __init__(self, arg):
		super(Thing, self).__init__()
		self.arg = arg


	def Look(args):
		print(description)
		return False

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
