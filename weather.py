import bs4 as bs
import urllib.request as req
"""This script when given the name of the departure and arrival airport, returns the metar for both airports"""


def departure(depart="KIAD"):
    source = req.urlopen(
        "https://www.aviationweather.gov/metar/data?ids="+depart.lower()).read()
    soup = bs.BeautifulSoup(source, "lxml")
    return soup.find("code").string


def arrival(arrive="KJFK"):
    source = req.urlopen(
        "https://www.aviationweather.gov/metar/data?ids="+arrive.lower()).read()
    soup = bs.BeautifulSoup(source, "lxml")
    return soup.find("code").string
