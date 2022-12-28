import argparse
import sys

from .hdfviewer import show, show_all

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--group", nargs='+', help="show specific groups")
    parser.add_argument("-v", "--verbose", help="show groups verbosely", action="store_true")
    parser.add_argument("hdf", help="HDF file path")
    args = parser.parse_args()
    if args.group:
        show(args.hdf, args.group, verbose=args.verbose)
    else:
        show_all(args.hdf, verbose=args.verbose)
