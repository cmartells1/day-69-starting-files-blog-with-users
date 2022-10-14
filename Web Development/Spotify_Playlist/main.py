import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"

entered_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(f"{URL}/{entered_date}")
billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, "html.parser")
song_name_h3 = soup.findAll(name='h3', class_='a-no-trucate')
song_list = [song.getText().strip() for song in song_name_h3]
