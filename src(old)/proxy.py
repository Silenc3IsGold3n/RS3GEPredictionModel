import time
import threading

proxy_List = []
proxy_Available = []

def get_proxy_list():
	return proxy_List

def populate_proxy_List():
	global proxy_List
	file = open('proxyList','r')
	proxy_List = file.read().splitlines()
	file.close()
	for i in proxy_List:
		proxy_Available.append(True)
	
def reset_proxy_list():
	for i in range (0,len(proxy_Available)):
		proxy_Available[i] = True
	
def get_available_proxy():
	for i in range (0,len(proxy_Available)):
		if (proxy_Available[i] == True):
			proxy_Available[i] = False
			return proxy_List[i]
	reset_proxy_list()
	return ''
