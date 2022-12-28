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
