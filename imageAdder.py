
# pip install beautifulsoup4 lxml
from bs4 import BeautifulSoup
import requests
import json

headers = {
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"
}

with open("anime2.json", "r+", encoding="utf-8") as json_file:                      
    anime = json.load(json_file)

i = 700
productInfo = []
while i<1000:

    website = requests.get(f"https://myanimelist.net/topanime.php?type=bypopularity&limit={i}", headers=headers)
    src = website.text
    soup = BeautifulSoup(src, "lxml")

    animeNames = soup.find_all(class_="fl-l fs14 fw-b anime_ranking_h3")

    for name in animeNames:
        link = name.find("a")
        sorc = link["href"]
        name = link.string

        newWebsite = requests.get(f"{sorc}", headers=headers)
        src2 = newWebsite.text
        soup2 = BeautifulSoup(src2, "lxml")
        if soup2.find(class_="lazyload"):
            img = soup2.find(class_="lazyload")["data-src"]
            print(name, img)

            if name in anime:
                anime[name]["bigImage"] = img

    print(i)
    with open("anime2.json", "w", encoding="utf-8") as file:
     json.dump(anime, file, indent=4, ensure_ascii=False)
    i+=50