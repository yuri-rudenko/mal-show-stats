from bs4 import BeautifulSoup
import requests
import json
import re

def animeToObject(link):

    print(link)

    headers = {
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"
    }

    website = requests.get(f"{link}", headers=headers)
    src = website.text
    soup = BeautifulSoup(src, "lxml")
    name = ''
    rating = ''
    year = ''
    members = ''
    popularity = ''
    type = ''
    studio = ''
    themes = []
    geners = []

    try:
        if soup.find(class_="title-name h1_bold_none"):
            name = soup.find(class_="title-name h1_bold_none").find("strong").string
    except AttributeError:
        pass

    try:
        if soup.find(class_="score-label"):
            rating = soup.find(class_="score-label").string
    except AttributeError:
        pass

    try:
        if soup.find(class_="season"):
            year = soup.find(class_="season").find("a").string[-4:]
    except AttributeError:
        pass

    try:
        if soup.find(class_="numbers members"):
            members = soup.find(class_="numbers members").find("strong").string.replace(",", "")
    except AttributeError:
        pass

    try:
        if soup.find(class_="numbers popularity"):
            popularity = soup.find(class_="numbers popularity").find("strong").string[1:]
    except AttributeError:
        pass

    try:
        if soup.find(class_="information type"):
            type = soup.find(class_="information type").find("a").string
    except AttributeError:
        pass

    try:
        if soup.find(class_="information studio author"):
            studio = soup.find(class_="information studio author").find("a").string
    except AttributeError:
        pass

    leftInfo = soup.find_all(class_="spaceit_pad")

    for el in leftInfo:

        if el.find(class_="dark_text").string == "Episodes:":
            episodes = el.find(class_="dark_text").next_sibling.strip()
        if el.find(class_="dark_text").string == "Source:":
            source = el.find(class_="dark_text").next_sibling.strip()
        if el.find(class_="dark_text").string == "Genres:" or el.find(class_="dark_text").string == "Genre:":
            geners = []
            genersTemp = el.find_all("a")
            for gen in genersTemp:
                geners.append(gen.string)
        if el.find(class_="dark_text").string == "Themes:" or el.find(class_="dark_text").string == "Theme:":
            themes = []
            themesTemp = el.find_all("a")
            for theme in themesTemp:
                themes.append(theme.string)

        if el.find(class_="dark_text").string == "Favorites:":
            favorites = el.find(class_="dark_text").next_sibling.strip().replace(",", "")
            break
    if name != '':
        return {
            "name": name,
            "rating":rating,
            "year":year,
            "members":members,
            "popularity":popularity,
            "type":type,
            "studio":studio,
            "episodes":episodes,
            "source":source,
            "geners":geners,
            "themes":themes,
            "favorites":favorites,
            "userRating": 0,
            "peopleRated": 1,
            "avarageUserRaating": 0,
        }
    else:
        return "Error"