# -​*- coding: utf-8 -*​-

from modules.math import sum, sub
from modules.hello import hello_world
from modules.sql import get_data

import argparse


arg_parser = argparse.ArgumentParser(description='Oh Shit! script.')
arg_parser.add_argument('-v', '--verbose', action='store_true', help='Increase output verbosity')
subparsers = arg_parser.add_subparsers(dest='method', help='Sub-method help.')

parser_sum = subparsers.add_parser('sum', help='Sum help.')
parser_sum.add_argument('a', type=float, help='First number to sum.')
parser_sum.add_argument('b', type=float, help='Second number to sum.')
parser_sum.add_argument('c', type=float, nargs='*', default=[0], help='Second number to sum.')

parser_sub = subparsers.add_parser('sub', help='Sub help.')
parser_sub.add_argument('a', type=float, help='First number to sub.')
parser_sub.add_argument('b', type=float, help='Second number to sub.')

parser_hello = subparsers.add_parser('hello', help='Hello help.')

parser_data = subparsers.add_parser('data', help='Data help.')

args = arg_parser.parse_args()

if args.method == 'sum':
    if args.verbose:
        print "The sum of {a} and {b} equals {c}".format(a=args.a, b=args.b, c=sum(args.a, args.b, args.c))
    else:
        print sum(args.a, args.b, args.c)
elif args.method == 'sub':
    if args.verbose:
        print "The sub of {b} from {a} equals {c}".format(a=args.a, b=args.b, c=sub(args.a, args.b))
    else:
        print sub(args.a, args.b)
elif args.method == 'hello':
    if args.verbose:
        print "Hello Beautifully Verbose World!"
    else:
        print hello_world()
elif args.method == 'data':
    if args.verbose:
        print "BLA BLA BLA\n"
        print get_data()
    else:
        print get_data()