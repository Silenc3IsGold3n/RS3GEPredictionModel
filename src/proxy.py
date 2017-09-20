import time
import threading

proxy_List = []
proxy_Available = []

#def timer(i,time_Left):
	#current_time = 0
	#while time < time_Left:
def populate_proxy_available():
	file = open('proxyAvailable','r')
	for line in file.readlines():
		proxy_Available.append(line);
	file.close()
	
def populate_proxy_List():
	file = open('proxyList','r')
	for line in file.readlines():
		proxy_List.append(line);
	file.close()
	print(proxy_List)
def update_proxy_available(i):
	#need to append the file
def get_available_proxy():
	print(proxy_Available)
	for i in range (0,len(proxy_Available)):
		if (proxy_Available[i] == True):
			update_proxy_available(i)
			return proxy_List[i]
	return ''
	
populate_proxy_List()
populate_proxy_available()