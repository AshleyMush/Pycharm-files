import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

"""
get movies

list movie names
    return movie name

"""

#TODO get movie NAMES

response = requests.get(url=URL)
empire_website = response.text

soup  = BeautifulSoup(empire_website, "html.parser")

movie_names_list = soup.find_all(name="h3", class_= "title")

movie_names = []
movie_ranking = []

for movie in movie_names_list:
    movie_name = movie.get_text()
    movie_names.append(movie_name)

#LIST SLICING                  (START:STOP:STEP)
top_100_movies_INORDER =movie_names[::-1]
print(top_100_movies_INORDER)

for movie in top_100_movies_INORDER:
    with open("movies.txt", mode="a", encoding="utf-8") as file:
            file.write(movie + "\n")

