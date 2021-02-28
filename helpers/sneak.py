from os import listdir
from os.path import isfile, join, abspath

accept_list = ["mp3", "m4a"]

def list_files(path):
    bulk_files = [abspath(join( path, rec)) for rec in listdir(path) if isfile(join(path, rec))]
    _assorted = [rec for rec in bulk_files if rec.split(".")[-1] in accept_list]
    return(_assorted)

