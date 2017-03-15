class AdministrationUnit:
    def __init(self):
        self.components = {}
        self.name = ""

    def get_results(self):
        results = {}
        for comp in self.components.values():
            comp_res = comp.get_results()
            for name in comp_res:
                if name in results:
                    results[name] += comp.results[name]
                else:
                    results[name] = comp.results[name]
        return results

    def get_max_voters(self):
        max_voters = 0
        for comp in self.components.values():
            max_voters += comp.get_max_voters()
        return max_voters

    def get_given_cards(self):
        given_cards = 0
        for comp in self.components.values():
            given_cards += comp.get_given_cards()
        return given_cards

    def get_total_votes(self):
        total_votes = 0
        for comp in self.components.values():
            total_votes += comp.get_total_votes()
        return total_votes

    def get_invalid_votes(self):
        invalid_votes = 0
        for comp in self.components.values():
            invalid_votes += comp.get_invalid_votes()
        return invalid_votes

    def get_valid_votes(self):
        valid_votes = 0
        for comp in self.components.values():
            valid_votes += comp.get_valid_votes()
        return valid_votes
    def get_components(self):
        return self.components


class Voivodeship(AdministrationUnit):
    def __init__(self):
        self.components = {}
        self.name = ""


class Constituency(AdministrationUnit):
    def __init__(self):
        self.components = {}
        self.name = ""


class District(AdministrationUnit):
    def __init__(self):
        self.components = {}
        self.name = ""


class Commune(AdministrationUnit):
    def __init__(self):
        self.results = {}
        self.name = ""
        self.vot_circs = 0
        self.max_voters = 0
        self.code = 0
        self.given_cards = 0
        self.total_votes = 0
        self.invalid_votes = 0
        self.valid_votes = 0

    def get_results(self):
        return self.results

    def get_max_voters(self):
        return self.max_voters

    def get_given_cards(self):
        return self.given_cards

    def get_total_votes(self):
        return self.total_votes

    def get_invalid_votes(self):
        return self.invalid_votes

    def get_valid_votes(self):
        return self.valid_votes
