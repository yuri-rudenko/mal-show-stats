import json
import csv
# "Katanagatari": {
#         "name": "Katanagatari",
#         "rating": "8.31",
#         "year": "2010",
#         "members": "550736",
#         "popularity": "378",
#         "type": "TV",
#         "studio": "White Fox",
#         "episodes": "12",
#         "source": "Light novel",
#         "geners": [
#             "Action",
#             "Adventure",
#             "Romance"
#         ],
#         "themes": [
#             "Historical",
#             "Martial Arts"
#         ],
#         "favorites": "10835",
#         "userRating": 16,
#         "peopleRated": 2,
#         "avarageUserRating": 8.0,
#         "bigImage": "https://cdn.myanimelist.net/images/anime/1112/119225.jpg"
#     }
#

with open('anime2.json', 'r', encoding="utf-8") as json_file:
    anime = json.load(json_file)

year = {}
genres = {}

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

print(genres)

    #with open("csv/members.csv", "a", encoding="utf-8") as file:
    #    writer = csv.writer(file)
    #    writer.writerow()
    #with open("csv/type.csv", "a", encoding="utf-8") as file:
    #    writer = csv.writer(file)
    #    writer.writerow()
    #with open("csv/studio.csv", "a", encoding="utf-8") as file:
    #    writer = csv.writer(file)
    #    writer.writerow()
    #with open("csv/episodes.csv", "a", encoding="utf-8") as file:
    #    writer = csv.writer(file)
    #    writer.writerow()
    #with open("csv/source.csv", "a", encoding="utf-8") as file:
    #    writer = csv.writer(file)
    #    writer.writerow()
    #with open("csv/geners.csv", "a", encoding="utf-8") as file:
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
