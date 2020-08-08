import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
import numpy as np
from matplotlib import pyplot as plt
from json.decoder import JSONDecodeError
import pandas as pd
from math import pi

scope = 'user-library-read'

def analyzeTracks(tracks):
	averageBPM = 0
	totalBPM = 0
	BPMtrack = np.array([0])
	trackTitles = np.array([0])
	danceArray = np.array([0])
	valenceArray = np.array([0])
	speechArray = np.array([0])
	energyArray = np.array([0])
	instrumentalArray = np.array([0])
	sp = spotipy.Spotify(auth=token)
	for i, item in enumerate(tracks['items']):
		track = item['track']
		try:
			features = sp.audio_features(track['id'])
			featuresRefined = features[0]
			danceArray = np.append(danceArray, featuresRefined['danceability'])
			valenceArray = np.append(valenceArray, featuresRefined['valence'])
			speechArray = np.append(speechArray, featuresRefined['speechiness'])
			energyArray = np.append(energyArray, featuresRefined['energy'])
			instrumentalArray = np.append(instrumentalArray, featuresRefined['instrumentalness'])
			#print(features)
			#whole = (sp.audio_analysis(track['id']))

			# barX = np.array([0])
			# barY = np.array([0])
			# wholeBars = whole['beats']
			# for x in wholeBars:
			# 	barX = np.append(barX, [np.array(x['start'])])
			# 	barY = np.append(barY, [np.array(x['duration'])])

			# barX = np.delete(barX, 0)
			# barY = np.delete(barY, 0)
			# plt.title("start vs. duration")
			# plt.plot(barX, barY)
			# #plt.show()

			# segmentStart = np.array([0])
			# segmentLoudnessMax = np.array([0])
			# pitchOne = np.array([0])
			# pitchTwo = np.array([0])
			# pitchThree = np.array([0])
			# pitchFour = np.array([0])
			# pitchFive = np.array([0])
			# wholeSegments = whole['segments']
			# wholeSegments = np.delete(wholeSegments, 0)
			# for y in wholeSegments:
			# 	segmentStart = np.append(segmentStart, [np.array(y['start'])])
			# 	segmentLoudnessMax = np.append(segmentLoudnessMax, [np.array(y['loudness_max'])])
			# 	allTwelve = np.array(y['pitches'])
			# 	pitchOne = np.append(pitchOne, allTwelve[0])
			# 	pitchTwo = np.append(pitchTwo, allTwelve[1])
			# 	pitchThree = np.append(pitchThree, allTwelve[2])
			# 	pitchFour = np.append(pitchFour, allTwelve[3])
			# 	pitchFive = np.append(pitchFive, allTwelve[4])

			# segmentStart = np.delete(segmentStart, 0)
			# segmentLoudnessMax = np.delete(segmentLoudnessMax, 0)
			# pitchOne = np.delete(pitchOne, 0)
			# pitchTwo = np.delete(pitchTwo, 0)
			# pitchThree = np.delete(pitchThree, 0)
			# pitchFour = np.delete(pitchFour, 0)
			# pitchFive = np.delete(pitchFive, 0)
			# plt.title("start vs loudness")
			# plt.plot(segmentStart, segmentLoudnessMax)
			# #plt.show()
			# plt.title("start vs pitchOne")
			# plt.plot(segmentStart, pitchOne, "bo")
			# plt.plot(segmentStart, pitchTwo, "ro")
			# plt.plot(segmentStart, pitchThree, "go")
			# plt.plot(segmentStart, pitchFour, "co")
			# plt.plot(segmentStart, pitchFive, "mo")
			#plt.show()

			#---------
			#wholeSections = whole['sections']
			#wholeSections = np.delete(wholeSections, 0)
			#sectionTempos = np.array([0])
			#sectionStart = np.array([0])
			#sectionDurations = np.array([0])
			#for z in wholeSections:
			#	sectionTempos = np.append(sectionTempos, z['tempo'])
			#	sectionStart = np.append(sectionStart, z['start'])
			#	sectionDurations = np.append(sectionDurations, z['duration'])
			#----------

			#sectionStart = np.delete(sectionStart, 0)
			#sectionTempos = np.delete(sectionTempos, 0)
			#sectionDurations = np.delete(sectionDurations, 0)
			#plt.title("start vs tempo sections")
			#plt.ylim((np.amin(sectionTempos) - 5), (np.amax(sectionTempos) + 5))
			#plt.bar(sectionStart, sectionTempos, width = sectionDurations, align='edge', edgecolor='blue')
			#plt.show()

			#----------
			trackTitles = np.append(trackTitles, track['name'])
			#BPMtrack = np.append(BPMtrack, np.mean(sectionTempos))
			#totalBPM += np.mean(sectionTempos)
			#----------

		except TypeError:
			print("", end ="")

	#--------------
	#BPMtrack = np.delete(BPMtrack, 0)
	trackTitles = np.delete(trackTitles, 0)
	#averageBPM = totalBPM / (i + 1)
	#plt.title("tempos vs songs")
	#plt.ylim((np.amin(BPMtrack) - 5), (np.amax(BPMtrack) + 5))
	#plt.axhline(y=averageBPM, zorder=0)
	#plt.bar(trackTitles, BPMtrack, edgecolor = 'blue')
	danceArray = np.delete(danceArray, 0)
	valenceArray = np.delete(valenceArray, 0)
	speechArray = np.delete(speechArray, 0)
	energyArray = np.delete(energyArray, 0)
	instrumentalArray = np.delete(instrumentalArray, 0)
	plt.title("Danceability")
	plt.ylim(0, 1)
	plt.bar(trackTitles, danceArray, edgecolor = 'blue')
	plt.show()
	plt.title("Danceability vs. Mood")
	plt.xlabel("Danceability (low -> high)")
	plt.ylabel("Mood (sad -> happy)")
	plt.scatter(danceArray, valenceArray)
	for count, n in enumerate(trackTitles):
		dx = danceArray[count]
		dy = valenceArray[count]
		plt.annotate(n, xy=(dx, dy),
			xytext = (dx + 0.004, dy + 0.004))
	plt.show()
	#need five variables (one value for each)
	#dance, valence, tempo, energy, loudness
	categories = np.array(["dance", "valence", "speechiness", "energy", "instrumentalness"])
	N = 5
	values = np.array(
		[danceArray[5], 
		valenceArray[5], 
		speechArray[5], 
		energyArray[5], 
		instrumentalArray[5], 
		danceArray[5]])
	print(values)
	angles = [n / float(N) * 2 * pi for n in range(N)]
	angles += angles[:1]
	ax = plt.subplot(111, polar=True)
	plt.xticks(angles[:-1], categories, color='grey', size=8)
	ax.set_rlabel_position(0)
	plt.yticks([.25,.5,.75,1], [".25",".50",".75", "1"], color="grey", size=7)
	plt.ylim(0,1)
	ax.plot(angles, values, linewidth=1, linestyle='solid')	 
	ax.fill(angles, values, 'b', alpha=0.1)
	plt.show()
	#---------------

if __name__ == '__main__':
	if len(sys.argv) > 2:
		username = sys.argv[1]
		playlistSelected = sys.argv[2]
	else:
		print("Whoops, need your username!")
		print("usage: python user_playlists.py [username]")
		sys.exit()

	token = util.prompt_for_user_token(username, scope, client_id='6161afd415714a388660361ac42b170a',
	client_secret='ffeabedf273a44478e16fdcab38f1693', redirect_uri='http://google.com/')
	if token:
		sp = spotipy.Spotify(auth=token)
		playlists = sp.user_playlists(username)
		for playlist in playlists['items']:
			if playlist['owner']['id'] == username and playlistSelected == playlist['id']:
				results = sp.playlist(playlist['id'], fields="tracks,next")
				tracks = results['tracks']
				analyzeTracks(tracks)
	else:
		print("Can't get token for", username)