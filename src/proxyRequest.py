import json
import requests
import time
import proxy
import urllib3
import gsocketpool
import socket
from urllib3 import ProxyManager, make_headers
#from urllib3.contrib.socks import SOCKSProxyManager
import threading



def run(url,prox):
	print(url)
	print(prox)
	http = ProxyManager(prox)	
	try:
		data = {'attribute': 'value'}
		encoded_data = json.dumps(data).encode('utf-8')
		req = http.request(
		'POST',
		url,
		#timeout = 3.0,
		body=encoded_data,
		headers={'Content-Type': 'html/text'})
		print(req.status)
		if(req.status == 404):
			print('Item Does not exist.')
			return
		if(req.status == 501):
			print('Proxy at api call limit')
			return
		if(req.status == 407):
			print('Authentication required')
			return
		if(req.status != 200):
			print('Unknown Status Code')
			print(req.status)
			return
	except:
		print('Request timed out.')
		return
		
		
	data = json.loads(req.data)
	req.release_conn()
		
	data = data['item']
	id = str(data['id'])
	print('ID: ' + id)
	file = open('ItemIds','a')
	file.write(id  + '\n')
	file.close()
			
