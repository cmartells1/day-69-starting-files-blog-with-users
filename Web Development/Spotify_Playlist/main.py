import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = "29b9325024724a4d90e8a11691e568b4"
CLIENT_SECRET = "0b687f9c80d642f9a904fc939b594f98"


entered_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = entered_date.split('-')[0]
print(year)
response = requests.get(f"{URL}/{entered_date}")
billboard_web_page = response.text
print(billboard_web_page)
soup = BeautifulSoup(billboard_web_page, "html.parser")
song_name_h3 = soup.findAll(name='h3', class_='a-no-trucate')
song_list = [song.getText().strip() for song in song_name_h3]
print(song_list)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth
    (client_id=CLIENT_ID,
     client_secret=CLIENT_SECRET,
     redirect_uri='http://localhost:8888/callback',
     scope='playlist-modify-private',
     cache_path='token.txt'
     )
)

user_id = sp.current_user()['id']
print(user_id)
