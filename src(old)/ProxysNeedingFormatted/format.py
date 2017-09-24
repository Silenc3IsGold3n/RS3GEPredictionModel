
data = []
data2 = []
data_final = []

file = open('unformatted','r')
data = file.read().splitlines()
print(data)
file.close()

for i in data:
	str = i
	str = 'http://' + str
	data2.append(str)
	
'''for i in data2:
	str = i
	j = len(str)-1
	#print(j)
	#print(str)
	while j > 0:
		if str[j] == ':':
			#print(j)
			#print(str)
			str = str[:j]
			break
		j-=1
	data_final.append(str)
print(data_final)
'''
file2 = open ('formatted','w+')
for i in data2:
	file2.writelines(i+'\n')
file2.close()