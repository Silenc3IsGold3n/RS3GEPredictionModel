import json
import requests
import time
#import urllib3
#import gsocketpool
import threading


		
def run(url,page):
	ids = []
	print(url)
	data = requests.get(url)
	if(data.status_code == 404):
		print('Item Does not exist.')
		return
	if(data.status_code == 200):
		if(len(data.text) == 0):
			print('Request Limit, Waiting five seconds.')
			time.sleep(5)
			return run(url,page)
	data = data.json()
	data = data['items']
	for i in data:	
		id = str(i['id'])
		print('ID: ' + id)
		ids.append(id)
	file = open('ItemIds','a')
	for i in ids:
		file.write(i  + '\n')
	file.close()
	if(len(data) == 12):
		newurl = url[:-1] + str(page+1)
		return run (newurl,page+1)
		