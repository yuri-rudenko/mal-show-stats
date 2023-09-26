
# pip install beautifulsoup4 lxml
from bs4 import BeautifulSoup
import requests
import json
import re
from fillUserList import fillUserList



headers = {
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"
}

anime = {}

with open('anime.json', 'r', encoding="utf-8") as json_file:
    anime = json.load(json_file)

used = [
    "Krutish",
    "Patiss0n",
    "Darconic",
    "Achmetha0626",
    "EyeSiN",
    "im_berny",
    "Kewpie2001",
    "Kiriyama_Rei18",
    "Krazyyyyy",
    "YamiNoTensai",
    "1Igo",
    "Rishon007",
    "thelambda",
    "Bugsbunnyfake",
    "Ashley___",
    "Rara019",
    "thisonebee",
    "Ks0345",
    "Pekyo",
    "Oubwio",
    "Kunasenpai",
    "Viscount-Zeimo",
    "Bolobos"
]
i = 0
input = [
    
]
users = []
while i<len(input):

    website = requests.get(f"https://myanimelist.net/profile/{input[i]}", headers=headers)
    src = website.text
    soup = BeautifulSoup(src, "lxml")

    favAnimeArr = []
    if soup.find(id="anime_favorites"):
        favAnime = soup.find(id="anime_favorites")
        favAnimeTitles = favAnime.find_all(class_="btn-fav")
        favAnimeArr = []
        for value in favAnimeTitles:
            favAnimeArr.append(value.get("title"))

    favMangaArr = []
    if soup.find(id="manga_favorites"):
        favManga = soup.find(id="manga_favorites")
        favMangaTitles = favManga.find_all(class_="btn-fav")
        favMangaArr = []
        for value in favMangaTitles:
            favMangaArr.append(value.get("title"))

    favCharactersArr = []
    if soup.find(id="character_favorites"):
        favCharacters = soup.find(id="character_favorites")
        favCharactersTitles = favCharacters.find_all(class_="btn-fav")
        favCharactersArr = []
        for value in favCharactersTitles:
            favCharactersArr.append({
                "name": value.find(class_="title").text,
                "anime": value.find(class_="users").text
            })

    users.append({
        "name": input[i],
        "link": f"https://myanimelist.net/profile/{input[i]}",
        "listLink": f"https://myanimelist.net/animelist/{input[i]}",
        "favAnime":favAnimeArr,
        "favManga":favMangaArr,
        "favCharacters":favCharactersArr,
        "ratedAnime": {}
    })

    print(i)
    users[i]["ratedAnime"] = []
    fillUserList(users[i], anime)
    with open(f"users/{users[i]['name']}.json", "w", encoding="utf-8") as file:
        json.dump(users[i], file, indent=4, ensure_ascii=False)
    i+=1



#print(users[0]["favCharacters"])
#with open("usersTest.json", "w", encoding="utf-8") as file:
#    json.dump(users, file, indent=4, ensure_ascii=False)