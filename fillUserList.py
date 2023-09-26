from bs4 import BeautifulSoup
import requests
import json
from animeToObject import animeToObject
import re
from time import sleep
from playwright.sync_api import sync_playwright

def fillUserList(user, anime):

    headers = {
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"
    }

    # soup = 1

    #with sync_playwright() as p:
    #    browser = p.chromium.launch()
    #    page = browser.new_page()
    #    page.goto(f"{user['listLink']}")
    #    soup = BeautifulSoup(page.content(), "lxml")
    #    browser.close()
#
    #animes = soup.find_all(class_="list-table-data")

    print(1)
    try:
        website=requests.get(f"https://myanimelist.net/animelist/{user['name']}/load.json?offset=0&status=7", headers=headers)
    except:
        return
    print(2)
    parsed = json.loads(website.text)
    i = 300

    while len(parsed) > 0:
        for an in parsed:
            try:
                #rating = an.find(class_="data score").find(class_="score-label").string.strip()
                if an["score"] != 0:

                    # name = an.find(class_="data title clearfix").find(class_="link sort").string.strip()

                    link = "https://myanimelist.net" + an["anime_url"]
                    
                    if(an["anime_title"] != 'None'):
                        user['ratedAnime'].append({
                            "name": an["anime_title"],
                            "userRating": an["score"]
                        })
                        print(an["anime_title"])
                        if str(an["anime_title"]) not in anime:
                            anime[str(an["anime_title"])] = animeToObject(link)
                        else:
                            anime[str(an["anime_title"])]["peopleRated"] += 1
                        anime[str(an["anime_title"])]["userRating"] += an["score"]
            except AttributeError:
                with open(f"{AttributeError}.txt", "w", encoding="utf-8") as file:
                    file.write(AttributeError)

        website=requests.get(f"https://myanimelist.net/animelist/{user['name']}/load.json?offset={i}&status=7", headers=headers)
        parsed = json.loads(website.text)
        i+=300
        
                    
    with open(f"anime.json", "w", encoding="utf-8") as file:
        json.dump(anime, file, indent=4, ensure_ascii=False)
    return