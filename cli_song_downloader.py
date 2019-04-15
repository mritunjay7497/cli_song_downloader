
#!/usr/bin/python3
from apiclient import discovery
import os
import time
import sys

#satisfying dependencies
print('FOR THIS SCRIPT TO WORK FOLLOWING DEPENDENCIES MUST BE MET\n')
print('[*]cURL\n')
print('[*]Youtube data v3 API enabled\n')
print('[*]API_KEY from youtube data v3 API\n')
print('[*]Googe API client python client\n')
print('[*]youtube-dl for audio conversion')


#checking dependencies
def check_dependencies():
	pkg[
	'which curl'
	'python3 -c apiclient'
	'which youtube-dl'
	]

	exit_status = [len(pkg)]
	ytdl_pkg = 'curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl && chmod u+rx /usr/local/bin/youtube-dl'
	for i in range(len(pkg)):
		status = os.system(pkg[i])
		time.sleep(1)
		exit_status[i] = os.system('echo $?')

	for i in range(len(pkg)):
		if(i==0 and exit_status[i]==1:)
			print("cURL not found. terminating program\n")
			print("install curl using\napt-get install curl")
			sys.exit(1)
		else if(i==0 and exit_status[i]==0):
			print("curl found.\nchecking for apiclient python3 library")

		if(i==1 and exit_status[i]==1):
			print("apiclient library for ppython3 not found")
			print("\ninstall it using 'python3 -m pip install apiclient'\n")
			print("terminating program")
			sys.exit(1)
		else if(i==1 and exit_status[i]==0):
			print("apiclient python3 library found.\nchecking for youtube-dl package")

		if(i==2 and exit_status[i]==1):
			print("youtube-dl not found.\n")
			print("run the following command to install it")
			print(ytdl_pkg)
			print("Terminating now\n")
			sys.exit(1)
		else if(i==2 and exit_status[i]==0):
			print("youtube-dl package found.\nAll dependencies met.\n")


print("\n[+]CHECKING DEPENDENCIES...\n")

				

#SONG DETAILS
print("enter the name of song\n")
song = str(input())
api_key = 'AIzaSyCb2W5-at7jz3SKDHRELTwNb5AtBn7KBKs'

#OBTAINING SONG LINK FROM YOUTUBE
youtube = discovery.build('youtube','v3',developerKey=api_key)
search_query = youtube.search().list(part="snippet",maxResults=1,q=song)
response = search_query.execute()
var = response['items'][0]['id']['videoId']
link="https://www.youtube.com/watch?v="+var

#CONVERTING YOUTUBE VIDEO IN TO AUDIO AND DOWNLOADING IT.
song_name = song.replace(" ", "_")
print('[+] THE SONG WILL BE SAVED AS:\n%s' % song_name)
download_cmd = 'youtube-dl '+link+' -o '+song_name
print("\n")
print("\n [+] DOWNLOADING SONG...\n")
print(download_cmd)
