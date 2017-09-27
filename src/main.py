import threading
import time
import gatherData
import printData
import getItemIds

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
urls = []
def get_Ids(x,y):
	for i in range(x, y):
		for j in alphabet:
			url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category='+ str(i) + '&alpha=' + str(j) + '&page=1'
			getItemIds.run(url,1)
			
def get_Data(x,y):
	global urls
	lock = threading.Lock()
	start_time = time.time()
	total_items_added = 0
	gatherData.load_urls()
	for i in range(x, y):
		url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category='+ str(i) + '&alpha=a'
		items_in_category = gatherData.get_items_in_category(url)
		print('Items in this category: ' + str(items_in_category))
		current_items = 0
		for j in alphabet:
			url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category='+ str(i) + '&alpha=' + str(j) + '&page=1'
			skip = False
			for u in urls:
				if(u == url):
					skip = True
					break
			if (skip == False):
				gatherData.run(url,1,lock)
				current_items = current_items + gatherData.get_current_items()
				print('Items added so far in category: ' + str(current_items) +'/'+str(items_in_category))
				gatherData.reset_current_items()
			else:
				print('Url has no items, skipping.')
				print('Items added so far in category: ' + str(current_items) +'/'+str(items_in_category))
			if (current_items == items_in_category):
				break
		total_items_added = total_items_added + current_items
	print('Total items added: ' + str(total_items_added))
	print('Toal time: ' + str((time.time() - start_time)) + ' seconds.')
	
class Main():
	global urls
	running = True
	#get list of urls that have no items
	file = open('pageswithnoitems','r')
	urls = file.read().splitlines()		
	file.close()
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
			#for i in range(0,1): 
				#lower = 0 + (i*18)
				#upper = (18+i) + (i*18)
			lower = 0
			upper = 37
			mythread = threading.Thread(name = "Thread-{}".format(1),target = get_Data,kwargs={'x': lower,'y': upper}) 
			mythread.start()
			time.sleep(.1)
			#get_Data(0,37)
			
		else:
			print('Unrecognized command use "help".')	
	while running == True:
		get_Input()
		
if __name__ == '__main__':
	main = Main()
		
		