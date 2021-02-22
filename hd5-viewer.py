import argparse
import sys

from pandas import HDFStore

def show(hdf_path, groups, verbose=False):
    with HDFStore(hdf_path) as hdf:
        for group in hdf.keys():
            if group[1:] in groups:
                print(group)
                print(hdf[group] if verbose else hdf[group].info(verbose=False))
                print('')

def show_all(hdf_path, verbose=False):
    with HDFStore(hdf_path) as hdf:
        if verbose:
            for group in hdf.keys():
                print(group)
                print(hdf[group])
                print('')
        else:
            print(hdf.info())

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
