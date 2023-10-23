
# pip install beautifulsoup4 lxml
from bs4 import BeautifulSoup
import requests
import json
import re
import os
from fillUserList import fillUserList



headers = {
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"
}

anime = {}

#with open('anime.json', 'r', encoding="utf-8") as json_file:
#    anime = json.load(json_file)

i = 0
# enter the usernames into this array separated by comma
input = [
    "ChatGPT_",
    "Patisson"
]
users = []
while i<len(input):

    website = requests.get(f"https://myanimelist.net/profile/{input[i]}", headers=headers)
    src = website.text
    soup = BeautifulSoup(src, "lxml")

    image = ''
    if soup.find(class_="user-image"):
        image = soup.find(class_="user-image").find("img")["data-src"]
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
        "profilePicture": image,
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

def custom_encoder(obj):
    if isinstance(obj, str):
        return obj.encode('utf-8').decode('unicode_escape')
    return obj

# Specify the folder containing your JSON files
folder_path = 'users'

# Initialize an empty list to store JSON objects
json_objects = []

for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                json_data = json.load(file)
                json_objects.append(json_data)
            except json.JSONDecodeError as e:
                print(f"Error reading {filename}: {e}")

output_file_path = 'users.json'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(json_objects, output_file, indent=4, ensure_ascii=False, default=custom_encoder)

print(f"Combined JSON file '{output_file_path}' created with {len(json_objects)} JSON objects.")





with open("anime.json", "r+", encoding="utf-8") as json_file:                      
    anime = json.load(json_file)
newAnime = anime.copy()
for key in anime:
    avg = (newAnime[key]["userRating"] / newAnime[key]["peopleRated"])
    newAnime[key]["avgUserRating"] = avg

with open("anime.json", "w", encoding="utf-8") as file:
     json.dump(newAnime, file, indent=4, ensure_ascii=False)

