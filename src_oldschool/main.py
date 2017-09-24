import threading
import time
import gatherData
import printData
import getItemIds

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def get_Ids(x,y):
	for j in alphabet:
		url = 'http://services.runescape.com/m=itemdb_oldschool/api/catalogue/items.json?category=1' + '&alpha=' + str(j) + '&page=1'
		getItemIds.run(url,1)
def get_Data():
	lock = threading.Lock()
	start_time = time.time()
	for j in alphabet:
		url = 'http://services.runescape.com/m=itemdb_oldschool/api/catalogue/items.json?category=1' + '&alpha=' + str(j) + '&page=1'
		gatherData.run(url,1,0,0,lock,False)
	print('Toal time: ' + str((time.time() - start_time)) + ' seconds.')
class Main():
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
			for i in range(0,2): 
				lower = 0 + (i*18)
				upper = (18+i) + (i*18)
				mythread = threading.Thread(name = "Thread-{}".format(i + 1),target = get_Ids,kwargs={'x': lower,'y': upper}) 
				mythread.start()
				time.sleep(.1)
		elif command == 'getData':
			#for i in range(0,2): 
				#lower = 0 + (i*18)
				#upper = (18+i) + (i*18)
				#mythread = threading.Thread(name = "Thread-{}".format(i + 1),target = get_Data,kwargs={'x': lower,'y': upper}) 
				#mythread.start()
				#time.sleep(.1)
			get_Data()
		else:
			print('Unrecognized command use "help".')	
	while running == True:
		get_Input()
		
if __name__ == '__main__':
	main = Main()
		
		