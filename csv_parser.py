import csv
from main_classes import *

voivodeship_dict = {}

def parse():
    voivodeship = 0
    constituency = 1
    commune_code = 2
    commune_name = 3
    district = 4
    vot_circs = 5
    max_voters = 6
    given_cards = 7
    total_votes = 8
    invalid_votes = 9
    valid_votes = 10

    with open("pkw2000.csv") as csv_results:
        next(csv_results, None)
        reader = csv.reader(csv_results)

        for row in reader:
            commune = Commune()

            commune.code = row[commune_code]
            commune.name = row[commune_name]
            commune.vot_circs = row[vot_circs]
            commune.max_voters = int(row[max_voters])
            commune.given_cards = int(row[given_cards])
            commune.total_votes = int(row[total_votes])
            commune.invalid_votes = int(row[invalid_votes])
            commune.valid_votes = int(row[valid_votes])

            if not row[voivodeship] in voivodeship_dict:
                new_voivodeship = Voivodeship()
                new_voivodeship.name = row[voivodeship]
                voivodeship_dict[row[voivodeship]] = new_voivodeship

            curr_voivodeship = voivodeship_dict[row[voivodeship]]

            if not row[constituency] in curr_voivodeship.components:
                new_const = Constituency()
                new_const.name = row[constituency]
                curr_voivodeship.components[row[constituency]] = new_const

            curr_const = curr_voivodeship.components[row[constituency]]

            if not row[district] in curr_const.components:
                new_distr = District()
                new_distr.name = row[district]
                curr_const.components[row[district]] = new_distr

            curr_distr = curr_const.components[row[district]]

            curr_distr.components[row[commune_name]] = commune

parse()
print(voivodeship_dict["MAZOWIECKIE"].get_max_voters())