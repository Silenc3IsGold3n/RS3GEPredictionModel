import threading
import gatherData


class MyThread(threading.Thread):
   # def run(self):
     #   print("{} started!".format(self.getName()))              # "Thread-x started!"
     #   time.sleep(1)                                      # Pretend to work for a second
      #  print("{} finished!".format(self.getName()))
	def run(self,x,y):
		for i in range(x, y):
			url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=' + str(i)
			print(url)
			gatherData.run(url)

if __name__ == '__main__':
	for i in range(0, 5):
		#threading.Thread(target=run()).start()
		mythread = MyThread(name = "Thread-{}".format(x + 1).run(1 + (i*1000),1000+(i*1000))) 
		mythread.start()