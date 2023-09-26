import json

file_path = r'D:\projects\Python study\mal-show-stats\users\im_berny.json'

with open(file_path, 'r', encoding="utf-8") as json_file:
    anime = json.load(json_file)

print(anime)