# Web Scraper to sample ancient Roman nomina/cognomina/praenomina from Wikipedia pages in order to identity person entities

import requests
from bs4 import BeautifulSoup
import json
import re


def read_data(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def write_data(file, data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def make_path_to_data(filename):
    return (
        "C:\\Users\\26shanic\\OneDrive - Hawken School\\other stuff\\Desktop\\Latin-Honors-Project-main\\data\\"
        + filename
    )


def get_nomina():
    url = "https://en.wikipedia.org/wiki/List_of_Roman_nomina"
    s = requests.get(url).content
    soup = BeautifulSoup(s, "lxml")
    final = []
    sections = soup.find_all("div", {"class": "div-col"})
    for section in sections:
        names = section.find_all("li")
        for name in names:
            try:
                name = name.text.split()[0].split("[")[0].strip()
                final.append(name)
            except:
                AttributeError
                print(name)
    write_data(make_path_to_data("nomina.json"), final)


def get_cognomina():
    url = "https://en.wikipedia.org/wiki/List_of_Roman_cognomina"
    s = requests.get(url).content
    soup = BeautifulSoup(s, "lxml")
    final = []
    sections = soup.find_all("p")
    for section in sections:
        names = section.find_all("a")
        for name in names:
            try:
                name = name.text.split()[0].strip()
                if name != "cognomina" and not re.match(r"\[[0-9]\]", name):
                    final.append(name)
            except:
                AttributeError
                print(name)
    write_data(make_path_to_data("cognomina.json"), final)

# Tf is this abomination
def get_praenomina():
    final = []
    with open(make_path_to_data("praenomina.txt"), "r", encoding="utf-8") as f:
        lines = f.readlines()

        for line in lines:
            line = line.replace("\n", "").replace(")", "")
            names = line.split("(")
            for name in names:
                if "," not in name and "or" not in name:
                    name = name.strip()
                    if name != "":
                        final.append(name)
                else:
                    if "," in name:
                        more = name.split(",")
                        for item in more:
                            item = item.strip()
                            if item != "":
                                final.append(item)
                    else:
                        more = name.split("or")
                        for item in more:
                            item = item.strip()
                            if item != "":
                                final.append(item)

    abs = []
    non_abs = []
    for name in final:
        if "." in name:
            abs.append(name)
        else:
            non_abs.append(name)
    abs = list(set(abs))
    non_abs = list(set(non_abs))
    final = list(set(final))

    abs.sort()
    non_abs.sort()
    final.sort()
    write_data(make_path_to_data("praenomina.json"), final)
    write_data(make_path_to_data("praenomina_abs.json"), abs)
    write_data(make_path_to_data("praenomina_nonabs.json"), non_abs)


if __name__ == "__main__":
    # Just run it and pray it doesnt break
    get_nomina()
    get_cognomina()
    get_praenomina()
