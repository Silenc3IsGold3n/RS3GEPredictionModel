import time
import threading

proxy_List = []
proxy_Available = []


def populate_proxy_List():
	file = open('proxyList','r')
	for line in file.readlines():
		proxy_List.append(line);
	file.close()
	for i in proxy_List:
		proxy_Available.append(True)
	
#def timer(i,time_Left):
	#current_time = 0
	#while time < time_Left:

	
def get_available_proxy():
	print(proxy_List)
	print(proxy_Available)
	for i in range (0,len(proxy_Available)):
		if (proxy_Available[i] == True):
			proxy_Available[i] = False
			proxyDict = {
			'http': '"' + proxy_List[i] + '"',
			'https':'"' +proxy_List[i].replace('http','https') + '"',	
			#'https':'"' +proxy_List[i]+ '"',				
			}
			return proxyDict
			#return proxy_List[i]
	return ''
