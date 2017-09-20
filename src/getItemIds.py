import json
import requests
import time
import proxy

def run_proxy(url):
	prox = proxy.get_available_proxy()
	print(str(prox))
	if(proxy == ''):
		return run(url)
	data = requests.get(url,proxies=prox)
	if(data.status_code == 404):
		print('Item Doesnt Exist.')
		return
	r = requests.post(url,data)
	if(r.status_code == 501):
		print('Requesting: ' + url + ' ' + 'with proxy.')
		return run_proxy(url)
	r.connection.close()
	
	if r:
		data = data.json()
		data = data['item']
		id = str(data['id'])
		print('ID: ' + id)
		file = open('ItemIds','a')
		file.write(id  + '\n')
		file.close()
def run(url):
	print(url)
	data = requests.get(url)
	#print(data.headers)
	#time.sleep(.01)
	if(data.status_code == 404):
		print('Item Doesnt Exist.')
		return
	r = requests.post(url,data)
	if(r.status_code == 501):
		#time.sleep(5)
		print('Requesting: ' + url + ' ' + 'with proxy')
		return run_proxy(url)
	#r = requests.post(url,data)
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
		