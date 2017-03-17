from jinja2 import Environment, PackageLoader, select_autoescape
from helper import check_and_create_path
from csv_parser import parse
from helper import generate_colors
from helper import generate_attendance


def generate_commune(commune, env):
    template = env.get_template("commune.html")

    check_and_create_path("build/commune")

    with open("build/commune/" + commune.get_escaped_name() + ".html", "w") as out:
        out.write(template.render(
            comm=commune,
            results=commune.get_sorted_results(),
            perc=commune.get_percentage(),
        ))


def generate_district(district, env, color):
    template = env.get_template("district.html")

    check_and_create_path("build/district")

    with open("build/district/" + district.get_escaped_name() + ".html", "w") as out:
        out.write(template.render(
            dist=district,
            results=district.get_sorted_results(),
            perc=district.get_percentage(),
            communes=sorted(district.components.items()),
            color=color
        ))

    for comm in district.components.values():
        generate_commune(comm, env)


def generate_constituency(constituency, env, color):
    template = env.get_template("constituency.html")

    check_and_create_path("build/constituency")

    with open("build/constituency/" + constituency.get_escaped_name() + ".html", "w") as out:
        out.write(template.render(
            const=constituency,
            results=constituency.get_sorted_results(),
            perc=constituency.get_percentage(),
            districts=sorted(constituency.components.items()),
            color=color
        ))

    for dist in constituency.components.values():
        generate_district(dist, env, color)


def generate_voivodeship(voivodeship, env, color):
    template = env.get_template("wojewodztwo.html")

    check_and_create_path("build/voivodeship")

    with open("build/voivodeship/" + voivodeship.get_escaped_name() + ".html", "w") as out:
        out.write(template.render(
            voivodeship=voivodeship,
            results=voivodeship.get_sorted_results(),
            perc=voivodeship.get_percentage(),
            constituencies=sorted(voivodeship.components.items()),
            color=color
        ))

    for const in voivodeship.components.values():
        generate_constituency(const, env, color)


def generate_basic_info(country, env):
    template_stylesheet = env.get_template("stylesheet.css")
    template_homepage = env.get_template("homepage_style.css")
    template_admunit = env.get_template("admunit_style.css")
    template_mapscript = env.get_template("map_script.js")

    with open("build/admunit_style.css", "w") as out:
        out.write(template_admunit.render())

    with open("build/homepage_style.css", "w") as out:
        out.write(template_homepage.render())

    with open("build/map_script.js", "w") as out:
        out.write(template_mapscript.render(
            attendance=generate_attendance(country)
        ))

    with open("build/stylesheet.css", "w") as out:
        out.write(template_stylesheet.render())


def generate_country(country, env):
    template_index = env.get_template("index.html")

    check_and_create_path("build")

    generate_basic_info(country, env)


    with open("build/index.html", "w") as out:
        out.write(template_index.render(
            country=country,
            results=country.get_sorted_results(),
            perc=country.get_percentage()
        ))

    for voivodeship in country.components.values():
        generate_voivodeship(voivodeship, env, generate_colors(country.get_results().keys()))


def generate():
    country = parse()
    env = Environment(
        loader=PackageLoader('app', 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    generate_country(country, env)
