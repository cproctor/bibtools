from os import listdir
from pathlib import Path
from itertools import chain
from pybtex.database import parse_file

def bib_reader(filename):
    "A generator which yields pbtex.database.Entry instances"
    try:
        return iter(parse_file(filename).entries.values())
    except Exception as e:
        print("Error reading bibtex file {}: {}".format(filename, e))
        return []

def bib_dir_reader(directory, ext=".bib"):
    "A generator for a directory of .bib files"
    bibs = filter(lambda f: f.endswith(ext), sorted(listdir(directory)))
    return chain.from_iterable(bib_reader(Path(directory) / b) for b in bibs)
