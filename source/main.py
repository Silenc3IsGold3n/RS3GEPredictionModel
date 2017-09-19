
import gatherData
import printData


for i in range(1, 100):
	url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=' + str(i)
	print(url)
	gatherData.run(url)
	
printData.run()