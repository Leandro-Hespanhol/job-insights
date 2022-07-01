import csv
from functools import lru_cache


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path, encoding="utf-8") as file:
        read_file = csv.DictReader(file)
        return list(read_file)
