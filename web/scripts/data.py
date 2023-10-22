import json
import csv


with open('anime2.json', 'r', encoding="utf-8") as json_file:
    anime = json.load(json_file)

year = {}
genres = {}
studios = {}
usualRating = {}

for title in anime.values():
    animeYear = title["year"]
    if animeYear != '':
        if animeYear in year:
            year[animeYear]["peopleRated"] += title["peopleRated"]
            year[animeYear]["userRating"] += title["userRating"]
            year[animeYear]["uniqueTitles"] += 1
        else:
            year[animeYear] = {
                "peopleRated": title["peopleRated"],
                "userRating": title["userRating"],
                "uniqueTitles": 1
            }
    
    genresThemes = [*title["geners"], *title["themes"]]

    if(len(genresThemes) != 0):
        for gen in genresThemes:
            if gen in genres:
                genres[gen]["peopleRated"] += title["peopleRated"]
                genres[gen]["userRating"] += title["userRating"]
                genres[gen]["uniqueTitles"] += 1
            else:
                genres[gen] = {
                    "peopleRated": title["peopleRated"],
                    "userRating": title["userRating"],
                    "uniqueTitles": 1  
                }
    animeStudio = title["studio"]        
    if(animeStudio != ''):
        if animeStudio in studios:
            studios[animeStudio]["peopleRated"] += title["peopleRated"]
            studios[animeStudio]["userRating"] += title["userRating"]
            studios[animeStudio]["uniqueTitles"] += 1
        else:
            studios[animeStudio] = {
                "peopleRated": title["peopleRated"],
                "userRating": title["userRating"],
                "uniqueTitles": 1  
            }
    name = title["name"]
    if(name != ''):
        if name in usualRating:
            usualRating[name]["peopleRated"] += title["peopleRated"]
            usualRating[name]["userRating"] += title["userRating"]
        else:
            usualRating[name] = {
                "peopleRated": title["peopleRated"],
                "userRating": title["userRating"],
                "members": title["members"],
                "globalRating": title["rating"]
            }
         

print(genres)

    #with open("csv/members.csv", "a", encoding="utf-8") as file:
    #    writer = csv.writer(file)
    #    writer.writerow()
    #with open("csv/episodes.csv", "a", encoding="utf-8") as file:
    #    writer = csv.writer(file)
    #    writer.writerow()
    #with open("csv/source.csv", "a", encoding="utf-8") as file:
    #    writer = csv.writer(file)
    #    writer.writerow()

    #with open("csv/rating.csv", "a", encoding="utf-8") as file:
    #    writer = csv.writer(file)
    #    writer.writerow()


with open("csv/year.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(("Year", "Populariy", "Rating", "Unique anime"))
for attr in year:
    with open("csv/year.csv", "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        avgRating = round(int(year[attr]["userRating"])/int(year[attr]["peopleRated"]), 3)
        writer.writerow((attr, year[attr]["peopleRated"], avgRating, year[attr]["uniqueTitles"]))

with open("csv/genres.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(("Genre", "Populariy", "Rating", "Unique anime"))
for attr in genres:
    with open("csv/genres.csv", "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        avgRating = round(int(genres[attr]["userRating"])/int(genres[attr]["peopleRated"]), 3)
        writer.writerow((attr, genres[attr]["peopleRated"], avgRating, genres[attr]["uniqueTitles"]))

with open("csv/studio.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(("Studio", "Populariy", "Rating", "Unique anime"))
for attr in studios:
    with open("csv/studio.csv", "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        avgRating = round(int(studios[attr]["userRating"])/int(studios[attr]["peopleRated"]), 3)
        writer.writerow((attr, studios[attr]["peopleRated"], avgRating, studios[attr]["uniqueTitles"]))

with open("csv/ratings.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(("Name", "User Populariy", "User Rating", "Global Popularity", "Global Rating",'misc'))

counter = 1
for attr in usualRating:
    with open("csv/ratings.csv", "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        avgRating = round(int(usualRating[attr]["userRating"])/int(usualRating[attr]["peopleRated"]), 3)
        writer.writerow((attr, usualRating[attr]["peopleRated"], avgRating, usualRating[attr]["members"], usualRating[attr]["globalRating"], f"{counter}"))
        counter += 1
