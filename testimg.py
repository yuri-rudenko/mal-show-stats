

from bs4 import BeautifulSoup
import requests
import json

headers = {
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"
}


website = requests.get(f"https://myanimelist.net/anime/18679/Kill_la_Kill", headers=headers)
src = website.text
soup = BeautifulSoup(src, "lxml")

photo = soup.find(class_="leftside").find(class_="lazyload")

print(photo["data-src"])