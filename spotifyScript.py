import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOauthError
from spotipy.client import SpotifyException

scope = 'user-library-read'
beginning = "python3 addToPlaylist.py cullejam19 4wgz2n9WADUTBcQijeMLhA"
#get username
#username = sys.argv[1]

#if token:
#	sp = spotipy.Spotify(auth=token)
#	results = sp.current_user_saved_tracks()
#	for item in results['items']:
#		track = item['track']
#		print(track['name'] + ' - ' + track['artists'][0]['name'])
#else:
#	print("Can't get toen for ", username)


def show_tracks(tracks, over100):
	for i, item in enumerate(tracks['items']):
		if over100:
			if i % 100 == 99:
				print('\n' * 1)
				print(beginning, end =" ")
		track = item['track']
		try:
			#sp = spotipy.Spotify(auth=token)
			#print(sp.audio_analysis(track['id']))
			print(track['id'], end = " ")
		except TypeError:
			print("", end ="")
		#print(track['name'])
		#print("   %d %32.32s %s" % (i, track['artists'][0]['name'],
		 #   track['name']))


if __name__ == '__main__':
	if len(sys.argv) > 1:
		username = sys.argv[1]
	else:
		print("Whoops, need your username!")
		print("usage: python user_playlists.py [username]")
		sys.exit()

	token = util.prompt_for_user_token(username, scope, client_id='6161afd415714a388660361ac42b170a',
	client_secret='ffeabedf273a44478e16fdcab38f1693', redirect_uri='http://google.com/')
	counter = 0
	songcount = 0

	if token:
		sp = spotipy.Spotify(auth=token)
		playlists = sp.user_playlists(username)
		print(beginning, end = " ")
		for playlist in playlists['items']:
			if playlist['owner']['id'] == username:
				over = False
				#print()
				#print(playlist['name'])
				#print ('  total tracks', playlist['tracks']['total'])
				counter += playlist['tracks']['total']
				#print(beginning, end = " ")
				#print(counter)
				if playlist['tracks']['total'] > 99:
					over = True
				if counter > 99:
					print('\n' * 1)
					print(beginning, end = " ")
					counter = playlist['tracks']['total']
					#print(counter)
				results = sp.playlist(playlist['id'], fields="tracks,next")
				tracks = results['tracks']
				show_tracks(tracks, over)
				while tracks['next']:
					tracks = sp.next(tracks)
					show_tracks(tracks, over)
	else:
		print("Can't get token for", username)