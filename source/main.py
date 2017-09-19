import threading
import gatherData


class MyThread(threading.Thread):
  
	def run(self,x,y):
		for i in range(x, y):
			url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=' + str(i)
			print(url)
			gatherData.run(url)

if __name__ == '__main__':
	#threading.Thread(target=run()).start()
	mythread = MyThread(name = "Thread-{}").run(2990,32000) 