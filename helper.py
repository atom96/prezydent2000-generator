from os.path import exists
from os import makedirs
from os.path import exists
from os import makedirs
from random import randint


def escape_diacritics(string):
    ltrPL = "ŻÓŁĆĘŚĄŹŃżółćęśąźń "
    ltrnoPL = "ZOLCESAZNzolcesazn_"
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


def generate_colors(candidates):
    color = {}
    for cand in candidates:
        col = "#%.6x" % randint(0, 0xFFFFFF)
        color[cand] = col

    return color


def generate_attendance(country):
    attendance = {}
    for voivodeship in country.components:
        attendance[voivodeship.lower()] = country.components[voivodeship].get_attendance()

    return attendance
