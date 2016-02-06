import argparse
import yaml
import pprint

from Thing import *
from Room import *
from Item import *

def status(args):
    print("I have some status")

def move(args):
    print("Moved to a place")

def act(args):
    print("Act in a way")

def look(args):
    with open('rooms.yml', 'r') as f:
        doc = yaml.load(f)
        txt = doc["room_0"]["desc"]
        print(txt)
    room_0 = Room(None, "adsf")

parser = argparse.ArgumentParser(description='Play the Game')

# show status by default
parser.set_defaults(func=status)

subparsers = parser.add_subparsers()

moveparse = subparsers.add_parser('move', help='move somewhere')
moveparse.add_argument('args', metavar='ARG', type=int, nargs='*',
                       help='everything else')
moveparse.set_defaults(func=move)

actparse = subparsers.add_parser('act', help='act')
actparse.add_argument('args', metavar='ARG', type=int, nargs='*',
                      help='everything else')
actparse.set_defaults(func=act)

lookparse = subparsers.add_parser('look', help='look')
lookparse.add_argument('args', metavar='ARG', type=int, nargs='*',
                       help='everything else')
lookparse.set_defaults(func=look)

with open('rooms.yml', 'r') as f:
    doc = yaml.load(f)

pp = pprint.PrettyPrinter(indent=4) # I don't know why a class has to be instantiated to pretty print...
# pp.pprint(doc)

roomDictionary = {}

for roomName, dictionary in doc.items():
    roomDictionary[roomName] = Room(dictionary)

# pp.pprint(roomDictionary)

if __name__ == "__main__":
    args = parser.parse_args()
    # func is set by set_defaults
    args.func(args)
