import json

with open("anime2.json", "r+", encoding="utf-8") as json_file:                      
    anime = json.load(json_file)
newAnime = anime.copy()
for key in anime:
    avg = (newAnime[key]["userRating"] / newAnime[key]["peopleRated"])
    newAnime[key]["avarageUserRating"] = avg


with open("anime2.json", "w", encoding="utf-8") as file:
     json.dump(newAnime, file, indent=4, ensure_ascii=False)