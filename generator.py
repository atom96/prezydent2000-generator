from jinja2 import Environment, PackageLoader, select_autoescape
from helper import check_and_create_path
from csv_parser import parse
from helper import generate_colors
from helper import generate_attendance


def generate_commune(commune, env, color):
    template = env.get_template("component.html")

    check_and_create_path("build/commune")

    with open("build/commune/" + commune.get_escaped_name() + ".html", "w") as out:
        out.write(template.render(
            unit=commune,
            results=commune.get_sorted_results(),
            perc=commune.get_percentage(),
            color=color,
            unit_type="gmina"
        ))


def generate_district(district, env, color):
    template = env.get_template("component.html")

    check_and_create_path("build/district")

    with open("build/district/" + district.get_escaped_name() + ".html", "w") as out:
        out.write(template.render(
            unit=district,
            results=district.get_sorted_results(),
            perc=district.get_percentage(),
            components=sorted(district.components.items()),
            color=color,
            unit_type="powiat",
            lower_unit="gmina",
            lower_unit_gen="gminach",
            lower_catalog="commune"
        ))

    for comm in district.components.values():
        generate_commune(comm, env, color)


def generate_constituency(constituency, env, color):
    template = env.get_template("component.html")

    check_and_create_path("build/constituency")

    with open("build/constituency/" + constituency.get_escaped_name() + ".html", "w") as out:
        out.write(template.render(
            unit=constituency,
            results=constituency.get_sorted_results(),
            perc=constituency.get_percentage(),
            components=sorted(constituency.components.items()),
            color=color,
            unit_type="okręg nr",
            lower_unit="powiat",
            lower_unit_gen="powiatach",
            lower_catalog="district"
        ))

    for dist in constituency.components.values():
        generate_district(dist, env, color)


def generate_voivodeship(voivodeship, env, color):
    template = env.get_template("component.html")

    check_and_create_path("build/voivodeship")

    with open("build/voivodeship/" + voivodeship.get_escaped_name() + ".html", "w") as out:
        out.write(template.render(
            unit=voivodeship,
            results=voivodeship.get_sorted_results(),
            perc=voivodeship.get_percentage(),
            components=sorted(voivodeship.components.items()),
            color=color,
            unit_type="województwo",
            lower_unit="okręg",
            lower_unit_gen="okręgach",
            lower_catalog="constituency"
        ))

    for const in voivodeship.components.values():
        generate_constituency(const, env, color)


def generate_basic_info(country, env):
    template_stylesheet = env.get_template("stylesheet.css")
    template_mobile = env.get_template("mobile_stylesheet.css")

    template_mapscript = env.get_template("map_script.js")

    with open("build/map_script.js", "w") as out:
        out.write(template_mapscript.render(
            attendance=generate_attendance(country)
        ))

    with open("build/stylesheet.css", "w") as out:
        out.write(template_stylesheet.render())

    with open("build/mobile_stylesheet.css", "w") as out:
        out.write(template_mobile.render())

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
