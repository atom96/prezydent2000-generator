from os.path import exists
from os import makedirs
from os.path import exists
from os import makedirs

def escape_diacritics(string):
    ltrPL = "ŻÓŁĆĘŚĄŹŃżółćęśąźń"
    ltrnoPL = "ZOLCESAZNzolcesazn"
    trantab = str.maketrans(ltrPL, ltrnoPL)

    return string.translate(trantab)

def get_percentage(results):
    votes_sum = sum(results.values())
    perc_res = {}
    for key, val in results.items():
        perc_res[key] = "%.2f" % (100 * val / votes_sum) + "%"
    return perc_res

def check_and_create_path(path):
    if not exists(path):
        makedirs(path)
