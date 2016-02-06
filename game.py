import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    subparsers = parser.add_subparsers()

    move = subparsers.add_parser('move', help='move somewhere')
    act = subparsers.add_parser('act', help='act')

    move.add_argument('args', metavar='ARG', type=int, nargs='+',
                      help='everything else')
    act.add_argument('args', metavar='ARG', type=int, nargs='+',
                     help='everything else')

    args = parser.parse_args()
    print(args.accumulate(args.integers))
