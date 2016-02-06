import argparse
import yaml
import pprint

PLAYER_FILE="player.yml"
from thing import *
from room import *
from item import *
from player import *

def status(args):
    print("I have some status")

def move(args):
    if len(args) == 0:
        print("You didn't specify anywhere to move to.")
    else:
        destination = args.pop(0)
        if player.move(destination):
            print("You move to the " + destination)
        else:
            print("You can't move there.")

def act(args):
    print("Act in a way")

def look(args):
    with open('rooms.yml', 'r') as f:
        doc = yaml.load(f)
    room = doc[player.data['room']]
    if len(args) == 0:
        txt = room["desc"]
    else:
        thingToLookAt = args.pop(0)
        if thingToLookAt in room["rooms"]:
            txt = room["rooms"][thingToLookAt]["desc"]
        else:
            txt = None
            for itemdict in room["items"]:
                if thingToLookAt in itemdict:
                    txt = itemdict[thingToLookAt][0]["desc"]
            if txt == None:
                txt = "You don't see " + thingToLookAt + "."
    print(txt)

def take(args):

def drop(args):

def use(args):


parser = argparse.ArgumentParser(description='Play the Game')

# show status by default
parser.set_defaults(func=status)

subparsers = parser.add_subparsers()

statusparse = subparsers.add_parser('status', help='show status')
statusparse.set_defaults(func=status)

moveparse = subparsers.add_parser('move', help='move somewhere')
moveparse.add_argument('args', metavar='room', nargs='*',
                       help='the room to move to')
moveparse.set_defaults(func=move)

actparse = subparsers.add_parser('act', help='act')
actparse.add_argument('args', metavar='ARG', nargs='*',
                      help='everything else')
actparse.set_defaults(func=act)

lookparse = subparsers.add_parser('look', help='look')

lookparse.add_argument('args', metavar='things', nargs='*',
                       help='things to look at')
lookparse.set_defaults(func=look)

takeparse = subparsers.add_parser('take', help='take an item')

takeparse.add_argument('args', metavar='items', help='the items you want to take', nargs='*')
takeparse.set_defaults(func=take)

dropparse = subparsers.add_parser('drop', help='drop an item')

dropparse.add_argument('args', metavar='items', help='the items you want to drop', nargs='*')
dropparse.set_defaults(func=drop)

useparse = subparsers.add_parser('use', help='use an item')

with open('rooms.yml', 'r') as f:
    doc = yaml.load(f)

pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(doc)

roomDictionary = {}

for roomName, dictionary in doc.items():
    roomDictionary[roomName] = Room(dictionary)

# pp.pprint(roomDictionary)

if __name__ == "__main__":
    player = Player.load(PLAYER_FILE)
    args = parser.parse_args()
    # func is set by set_defaults
    # print("Arguments are:\n") # debugging info
    # pp.pprint(args)
    args.func(args.args)
    player.save(PLAYER_FILE)
