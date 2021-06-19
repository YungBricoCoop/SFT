import os
import time
import keyboard
import requests

from rich.console import Console
from rich.progress import Progress, track

SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/api/token'
SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
SPOTIFY_POST_NEXT = "https://api.spotify.com/v1/me/player/next"
SPOTIFY_POST_PREVIOUS = "https://api.spotify.com/v1/me/player/previous"
SPOTIFY_POST_PAUSE = "https://api.spotify.com/v1/me/player/pause"
ACCESS_TOKEN = '***************'
setBar = False

def next_track():
	response = requests.post(SPOTIFY_POST_NEXT,headers={"Authorization": f"Bearer {ACCESS_TOKEN}"})

def previous_track():
	response = requests.post(SPOTIFY_POST_PREVIOUS,headers={"Authorization": f"Bearer {ACCESS_TOKEN}"})

def pause_track():
	response = requests.put(SPOTIFY_POST_PAUSE,headers={"Authorization": f"Bearer {ACCESS_TOKEN}"})	

def get_current_track(access_token):
    response = requests.get(SPOTIFY_GET_CURRENT_TRACK_URL,headers={"Authorization": f"Bearer {access_token}"} )
    json_resp = response.json()
    progress = round(json_resp['progress_ms']/1000)
    duration = round((json_resp['item']['duration_ms']-1000)/1000)
    track_name = json_resp['item']['name']
    artists = [artist for artist in json_resp['item']['artists']]
    artist_names = [artist['name'] for artist in artists][0]
    return [track_name,artist_names,progress,duration]

def main():
	clear = lambda: os.system('cls')
	clear()
	console = Console()
	lastSong = ""
	with Progress() as progress:	
		while True:
			if keyboard.is_pressed('f1'):
				next_track()
			if keyboard.is_pressed('f2'):
				previous_track()
			if keyboard.is_pressed('f3'):
				pause_track()
			t = get_current_track(ACCESS_TOKEN)
			if lastSong!= t[0] :
				lastSong = t[0]
				setBar = True
			if setBar:
				task1 = progress.add_task("[bold #f92672]Playing[/bold #f92672] [bold cyan]"+t[0]+" - "+t[1]+"[/bold cyan]" , total=t[3])
				setBar = False
			progress.update(task1, advance=1,completed=t[2])
			time.sleep(1)
if __name__ == '__main__':
    main()