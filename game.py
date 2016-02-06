import argparse


def move(args):
    print("Moved to a place")


def act(args):
    print("Act in a way")

def look(args):
    print("looked")

parser = argparse.ArgumentParser(description='Play the Game')

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

if __name__ == "__main__":
    args = parser.parse_args()
    # func is set by subcommand
    args.func(args)
