from csv_parser import parse

country = parse()
print(country.get_max_voters())
print(country.get_given_cards())
print(country.get_total_votes())
print(country.get_valid_votes())
print(country.get_invalid_votes())
print(country.get_attendance())

print(sorted(country.get_results().items(), reverse=True, key=lambda x: x[1]))