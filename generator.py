from jinja2 import Environment, PackageLoader, select_autoescape
from helper import escape_diacritics, get_percentage, check_and_create_path
from csv_parser import parse


def generate_voivodeship(voivodeship):
    results = voivodeship.get_results()
    sorted_results = sorted(results.items(), reverse=True, key=lambda x: x[1])
    env = Environment(
        loader = PackageLoader('app', 'templates'),
        autoescape = select_autoescape(['html', 'xml'])
    )
    template = env.get_template("wojewodztwo.html")

    check_and_create_path("build/voivodeship")

    with open("build/voivodeship/" + escape_diacritics(voivodeship.name.lower()) + ".html", "w") as out:
        out.write(template.render(
            voivodeship = voivodeship,
            results = sorted_results,
            perc = get_percentage(results)
        ))


def generate_country(country, env):
    template = env.get_template("index.html")
    results = country.get_results()
    sorted_results = sorted(results.items(), reverse=True, key=lambda x: x[1])

    check_and_create_path("build")
    with open ("build/index.html", "w") as out:
        out.write(template.render(
            country = country,
            results = sorted_results,
            perc = get_percentage(results)
        ))

    for voivodeship in country.components.values():
        generate_voivodeship(voivodeship)


def generate():
    country = parse()
    env=Environment(
        loader = PackageLoader('app','templates'),
        autoescape = select_autoescape(['html','xml'])
    )

    generate_country(country, env)


