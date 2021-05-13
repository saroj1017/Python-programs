import json
import requests
from bs4 import BeautifulSoup as BS

url = 'https://www.empireonline.com/movies/features/best-movies-2'
r = requests.get(url)
r.raise_for_status()
soup = BS(r.text, features="html.parser")
obj = soup.select_one('script#__NEXT_DATA__')
data = json.loads(obj.contents[0])
# print(data)
# generator expression avoids storing the entire list in memory
# however it can only be consumed once
articles = (
    item for key, item in data['props']['pageProps']['apolloState'].items()
    if key.startswith('ImageMeta')
)

article_list = [*(e['titleText'] for e in articles)]
print(article_list)
with open("movies.txt", mode="w") as file:
     for movie in article_list:
         file.write(f"{movie}\n")
