from requests import get
from bs4 import BeautifulSoup
import json

url = 'https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&count=100'

response = get(url, headers = {"Accept-Language": "en-US"})

hsoup = BeautifulSoup(response.text, "html.parser")

movies = hsoup.find_all('div', class_ = 'lister-item mode-advanced')

data = {}
data['movies'] = []
ID = 1
for movie in movies:
    name = movie.h3.a.text
    span_genre = movie.find('span', class_ = 'genre')
    genre = span_genre.text
    desc = movie.find_all('p', class_ = 'text-muted')
    description = desc[1].text
    data['movies'].append({
        'id': ID,
        'name' : name,
        'genre' : genre.split(',')[0].strip(),
        'description' : description.strip()
    })
    ID += 1


try:
    with open('storage/movies.txt', 'x') as outfile:
        json.dump(data, outfile)
except FileExistsError:
    with open('storage/movies.txt', 'w') as outfile:
        json.dump(data, outfile)