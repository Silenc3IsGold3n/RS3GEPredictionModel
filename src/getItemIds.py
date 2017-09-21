import json
import requests
import time
import proxy
import urllib3
import gsocketpool
import socket
from urllib3 import ProxyManager, make_headers
from urllib3.contrib.socks import SOCKSProxyManager

def test_proxy(url):
	#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	prox = proxy.get_available_proxy()
	#print(prox)
	#print(socket.getaddrinfo('www.services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=2',80, 0, 0, socket.IPPROTO_TCP))
	#s.connect(('http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=2',80))
	#request = b"GET / HTTP/1.1\nHost: http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=2\n\n"
	#s.send(request)
	#result = s.recv(10000)
	#print(result)
	
	default_headers = make_headers(proxy_basic_auth='user:pass')

	http = ProxyManager('http://35.189.104.232',timeout = 3)
	#http = SOCKSProxyManager('socks5://46.38.40.19:1080')
	#http = urllib3.PoolManager()
	try:
		data = {'attribute': 'value'}
		encoded_data = json.dumps(data).encode('utf-8')
		req = http.request(
		'POST',
		'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=2',
		body=encoded_data,
		headers={'Content-Type': 'html/text'})
	except:
		print('max entries')
		return
	print(req.data)
	data = json.loads(req.data.decode('utf-8'))
	
	print(data['item'][])
	#res = http.response('http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=2')
	#for i in req.data:
	#	print(i)
	#print(res)
	req.release_conn()
	#req.add_header('Content-Type', 'HTMl\json')
	
	#print (str(json.dumps(data,indent = 4)))
	#response = urllib3.urlopen(req, json.dumps(data))
	#data = requests.get(url,proxies=prox)
	#print(data)
	
	#print(socket.getaddrinfo('http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=2', 80))
	#print(prox)

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
	#print(data.content)
	#time.sleep(.01)
	#print(data.raw._fp.fp.raw._sock)
	if(data.status_code == 404):
		print('Item Doesnt Exist.')
		return
	r = requests.post(url,data)
	if(r.status_code == 501):
		print('Requesting: ' + url + ' ' + 'with proxy')
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
		