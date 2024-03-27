# TODO: actually finish this shit


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
