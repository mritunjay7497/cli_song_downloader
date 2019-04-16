
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

pkg=[
	'which curl',
	'python3 -c "import apiclient"',
	'which youtube-dl'
	]

exit_status = ['0','0','0']

#checking dependencies
def check_dependencies():
	
	ytdl_pkg = 'curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl && chmod u+rx /usr/local/bin/youtube-dl'
	for i in range(3):
		status = os.system(pkg[i])
		print(status)
		time.sleep(1)
		exit_status[i] = os.system('echo $?')

	for i in range(len(pkg)):
		if(i==0 and exit_status[i]==1):
			print("cURL not found. terminating program\n")
			print("install curl using\napt-get install curl")
			sys.exit(1)
		elif(i==0 and exit_status[i]==0):
			print("curl found.\nchecking for apiclient python3 library")

		if(i==1 and exit_status[i]==1):
			print("apiclient library for python3 not found")
			print("\ninstall it using 'python3 -m pip install apiclient'\n")
			print("terminating program")
			sys.exit(1)
		elif(i==1 and exit_status[i]==0):
			print("apiclient python3 library found.\nchecking for youtube-dl package")

		if(i==2 and exit_status[i]==1):
			print("youtube-dl not found.\n")
			print("run the following command to install it")
			print(ytdl_pkg)
			print("Terminating now\n")
			sys.exit(1)
		elif(i==2 and exit_status[i]==0):
			print("youtube-dl package found.\nAll dependencies met.\n")


print("\n[+]CHECKING DEPENDENCIES...\n")
check_dependencies()

				
#SONG DETAILS
print("enter the number of song you want to download:\n")
# song = str(input())
n=int(input())
song = []
i=0
print("enter the name of songs you want to download:\n")
while(i<n):
	song_name = str(input())
	song.append(song_name)
	i+=1

print("The songs requested by the user are:\n")
print(song)
print('\n\n\n')

#OBTAINING SONG LINK FROM YOUTUBE
api_key = 'PASTE THE YOUTUBE DATA V3 API KEY HERE' #PASTE THE YOUTUBE DATA V3 API KEY HERE.
youtube = discovery.build('youtube','v3',developerKey=api_key)
val=0
while(val<len(song)):
	search_query = youtube.search().list(part="snippet",maxResults=1,q=song[val])
	response = search_query.execute()
	var = response['items'][0]['id']['videoId']
	link="https://www.youtube.com/watch?v="+var

	#CONVERTING YOUTUBE VIDEO IN TO AUDIO AND DOWNLOADING IT.
	song[val] = song[val].replace(" ", "_")
	print("[+] DOWNLOADING SONG... \t%s\n" % song[val])
	print('[+] THE SONG WILL BE SAVED in /root/Music/'+song[val]+'\n')
	download_cmd = 'youtube-dl '+link+' -f bestaudio'+' -o /root/Music/'+song[val]
	os.system(download_cmd)
	print('\n\n\n')
	val+=1
	#DOWNLOAD CHECK
	

