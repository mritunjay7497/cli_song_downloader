#!/usr/bin/python3
# from urllib.request import urlopen
import requests
import urllib
# from bs4 import BeautifulSoup
from apiclient import discovery
from selenium import webdriver


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
print(link)

# html = urlopen("https://www.ytmp3.cc")
# bsobj = BeautifulSoup(html,'html.parser')
# print (bsobj)

# for link in bsobj.findAll('a'):
# 	if 'href' in link.attrs:
# 		#print(link.attrs['href'])
# 		link_matrix =link.attrs['href']
# url = "https://ytmp3.cc/"
# values = {'input':link}
# r = requests.post(url,params=values)
# html = r.content
# print(html)

#DOWNLOADING VIDEO
# quality = 'mp3_256Kbps'
# download_url = 'https://www.youtubnow.com/watch/?v='
# final_url = download_url+var+'&f='+quality
# https://www.youtubnow.com/watch/?v=eJnQBXmZ7Ek&f=mp3_256Kbps
# print(final_url)

url = "https://ytmp3.cc"
data = {"link":link}
print(data)
r = requests.post(url,data)
with open("requests_results.html","wb") as f:
	f.write(r.content)