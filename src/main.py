import threading
import time
import gatherData
import printData
import getItemIds
import proxy


def get_Ids(x,y):
	for i in range(x, y):
		url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=' + str(i)
		getItemIds.test_proxy(url)
def get_Data(x,y):
		for i in range(x, y):
			url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=' + str(i)
			print(url)
			gatherData.run(url)
class Main():
	print('Loading proxy list.')
	proxy.populate_proxy_List()
	print('Done!')
	running = True
	def get_Input():
		print('Enter Command:',end='')
		command = input()
		if command == 'help':
			print('"getData": Grabs all items on the Grand Exchange and stores their info into a database.')
			print('"printData": Prints all data in the DataBase')
			print('"getIds": Gets all the ids of items that actually exist on the GE.')
		elif command == 'exit':
			running = False
			exit()
		elif command == 'printData':
			printData.run()
		elif command == 'getIds':
			#for i in range(0,1): 
				#lower = 0 + (i*10)
				#upper = 10 + (i*10)
				#mythread = threading.Thread(name = "Thread-{}".format(i + 1),target = get_Data,kwargs={'x': lower,'y': upper}) 
				#mythread.start()
				#time.sleep(.1)
			get_Ids(0,1)
		elif command == 'getData':
			for i in range(0,4): 
				lower = 0 + (i*1000)
				upper = 1000 + (i*1000)
				mythread = threading.Thread(name = "Thread-{}".format(i + 1),target = get_Data,kwargs={'x': lower,'y': upper}) 
				mythread.start()
				time.sleep(.1)
		else:
			print('Unrecognized command use "help".')	
	while running == True:
		get_Input()
		
if __name__ == '__main__':
	main = Main()
		
		