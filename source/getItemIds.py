import json
import requests
import time

def run(url):
	data = requests.get(url)
	time.sleep(.01)
	if(data.status_code == 404):
		print('Item Doesnt Exist.')
		return
	if(data.status_code == 501):
		print('TODO')
	r = requests.post(url,data)
	print(r)
	r.connection.close()
	if r:
		data = data.json()
		#print (str(json.dumps(data,indent = 4)))
		data = data['item']
		id = str(data['id'])
		print('ID: ' + id)
		file = open('ItemIds','a')
		file.write(id  + '\n')
		file.close()
		