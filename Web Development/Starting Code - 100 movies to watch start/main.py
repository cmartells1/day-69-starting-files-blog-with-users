import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
movie_web_page = response.text

#Need to use soup.prettify() in order to see the goodness
soup = BeautifulSoup(movie_web_page, "html.parser")
all_movies = soup.findAll(name='h3' ,class_='title')
movie_titles = [movie.getText() for movie in all_movies]
reversed_movie_title_list = movie_titles[::-1]#this syntax reverses the order of the list with splice
# for movie in reversed(movie_titles):
#     title = movie.getText()
#     reversed_movie_title_list.append(title)

with open('movie_titles.txt', mode='w', encoding='utf-8') as file:
    for title in reversed_movie_title_list:
        file.write(f"{title} \n")