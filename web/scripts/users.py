# Most boring/unique taste
# Best/worst taste
# Newbie/oldie anime fan
# Biggest genre fan
# Biggest studio fan
# Biggest/Smallest avrage/amount of anime watched
# Biggest AoT fan

import json
import csv

with open('anime2.json', 'r', encoding="utf-8") as json_file:
    anime = json.load(json_file)

with open('users.json', 'r', encoding="utf-8") as json_file:
    users = json.load(json_file)

userArr = {}

for user in users:
    cur = user
    userArr[cur["name"]] = {
        "name": user["name"],
        "animeWatched": len(user["ratedAnime"]),
        "avgPopularity": "",
        "avgDeviation": "",
        "avgYear": "",
        "avgRating": "",
        "avgAvgRating": "",
        "aotIndex": 0,
        #"genres": [
        #    {
        #        "genre": "",
        #        "fanIndex": ""
        #    }
        #],
        #"studios": [
        #    {
        #        "studio": "",
        #        "fanIndex": ""
        #    }
        #],
    }
    popularity = 0
    deviation = 0
    year = 0
    yearCount = 0
    rating = 0
    avgRating = 0
    aotIndex = 0
    for title in user["ratedAnime"]:
        show = anime[str(title["name"])]
        popularity += int(show["popularity"])
        deviation += abs(title["userRating"]-float(show["rating"]))
        if show["year"] != "":
            year+=int(show["year"])
            yearCount+=1
        rating += title["userRating"]
        avgRating += float(show["rating"])
        if "Shingeki no Kyojin" in str(show["name"]):
            aotIndex += title['userRating']
            
    num = userArr[cur["name"]]["animeWatched"]
    userArr[cur["name"]]["avgPopularity"] = round(popularity/num)
    userArr[cur["name"]]["avgDeviation"] = round(deviation/num, 4)
    userArr[cur["name"]]["avgYear"] = round(year/yearCount, 2)
    userArr[cur["name"]]["avgAvgRating"] = round(avgRating/num, 3)
    userArr[cur["name"]]["avgRating"] = round(rating/num, 3)
    userArr[cur["name"]]["aotIndex"] = aotIndex

userArr[cur["name"]] = {
        "name": user["name"],
        "animeWatched": len(user["ratedAnime"]),
        "avgPopularity": "",
        "avgDeviation": "",
        "avgYear": "",
        "avgRating": "",
        "avgAvgRating": "",
        "aotIndex": 0,
}
with open("csv/users.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(("Name", "animeWatched", "avgPopularity", "avgDeviation", "avgYear", "avgRating", "avgAvgRating", "aotIndex"))
for user in userArr:
    with open("csv/users.csv", "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow((user, userArr[user]["animeWatched"], userArr[user]["avgPopularity"], userArr[user]["avgDeviation"], userArr[user]["avgYear"], userArr[user]["avgRating"], userArr[user]["avgAvgRating"], userArr[user]["aotIndex"]))