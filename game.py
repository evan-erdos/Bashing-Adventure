import argparse


def status(args):
    print "I have some status"


def move(args):
    print "Moved to a place"


def act(args):
    print "Act in a way"

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
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

if __name__ == "__main__":
    args = parser.parse_args()
    # func is set by set_defaults
    args.func(args)
