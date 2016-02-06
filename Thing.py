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

