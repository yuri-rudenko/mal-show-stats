import json
import csv
import math

with open('anime2.json', 'r', encoding="utf-8") as json_file:
    anime = json.load(json_file)

with open('users.json', 'r', encoding="utf-8") as json_file:
    users = json.load(json_file)

genre_list = []
studio_list = []

for title_key, title in anime.items():
    genresThemes = [*title["geners"], *title["themes"]]

    if len(genresThemes) != 0:
        for gen in genresThemes:
            found = False
            for genre in genre_list:
                if genre["name"] == gen:
                    genre["peopleRated"] += title["peopleRated"]
                    genre["userRating"] += title["userRating"]
                    genre["uniqueTitles"] += 1
                    found = True
                    break
            if not found:
                genre_list.append({
                    "name": gen,
                    "peopleRated": title["peopleRated"],
                    "userRating": title["userRating"],
                    "uniqueTitles": 1,
                    "users": {},
                })

    animeStudio = title["studio"]
    if animeStudio != '':
        found = False
        for studio in studio_list:
            if studio["name"] == animeStudio:
                studio["peopleRated"] += title["peopleRated"]
                studio["userRating"] += title["userRating"]
                studio["uniqueTitles"] += 1
                found = True
                break
        if not found:
            studio_list.append({
                "name": animeStudio,
                "peopleRated": title["peopleRated"],
                "userRating": title["userRating"],
                "uniqueTitles": 1,
                "users": {},
            })

for user in users:
    for title in user["ratedAnime"]:
        show = anime.get(str(title["name"]))
        if show and show["studio"]:
            studio_name = show["studio"]
            for studio in studio_list:
                if studio["name"] == studio_name:
                    if user["name"] not in studio["users"]:
                        studio["users"][user["name"]] = {
                            "studioRating": title["userRating"],
                            "amount": 1,
                        }
                    else:
                        studio["users"][user["name"]]["studioRating"] += title["userRating"]
                        studio["users"][user["name"]]["amount"] += 1

        genresThemes = [*show["geners"], *show["themes"]]

        if len(genresThemes) != 0:
            for gen in genresThemes:
                for genre in genre_list:
                    if genre["name"] == gen:
                        if user["name"] not in genre["users"]:
                            genre["users"][user["name"]] = {
                                "genreRating": title["userRating"],
                                "amount": 1,
                            }
                        else:
                            genre["users"][user["name"]]["genreRating"] += title["userRating"]
                            genre["users"][user["name"]]["amount"] += 1

genre_list.sort(key=lambda x: x["peopleRated"], reverse=True)

studio_list.sort(key=lambda x: x["peopleRated"], reverse=True)

with open("csv/userGenres.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(("Name", *[genre["name"] for genre in genre_list]))
with open("csv/userGenres.csv", "a", encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    for user in users:
        ratingsArr = []
        for genre in genre_list:
            if(user["name"] in genre["users"]):
                curUser = genre["users"][user["name"]]
                ratingsArr.append(round(curUser["genreRating"]/(math.sqrt(curUser["amount"])*math.sqrt(len(user["ratedAnime"]))), 2))
            else:
                ratingsArr.append(0)

        writer.writerow((user["name"], *ratingsArr))

with open("csv/userStudios.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(("Name", *[studio["name"] for studio in studio_list]))
with open("csv/userStudios.csv", "a", encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    for user in users:
        ratingsArr = []
        for studio in studio_list:
            if(user["name"] in studio["users"]):
                curUser = studio["users"][user["name"]]
                ratingsArr.append(round(curUser["studioRating"]/(math.sqrt(curUser["amount"])*math.sqrt(len(user["ratedAnime"]))), 2))
            else:
                ratingsArr.append(0)

        writer.writerow((user["name"], *ratingsArr))
