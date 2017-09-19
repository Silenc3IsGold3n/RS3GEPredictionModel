
import gatherData

for i in range(0, 100):
	url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=' + str(i)
	print(url)
	gatherData.run(url)
#item_Record = Item()