class Item():
	#Icon = ''
	#Icon_large = ''
	Id = 0
	Type = '' 
	Name = ''
	Members = False
	Current_trend = ''
	Current_price = 0
	Today_trend = ''
	Today_price = 0
	
	def __init__(self,id,type, name, current_trend,current_price,today_trend,today_price,members):
		#self.Icon = icon
		#self.Icon_large = icon_large
		self.Id = id
		self.Type = type
		self.Name = name
		if members == 'true':
			members = True
		else:
			members = False
		self.Members = members
		
		self.Current_trend = current_trend
		current_price = str(current_price)
		current_price = current_price.replace(',','')
		current_price = current_price.replace(' ','')
		if current_price[-1:] == 'm':
			current_price = float(current_price[0:-1]) * 1000000
		elif current_price[-1:] == 'k':
			current_price = float(current_price[0:-1]) * 1000
		elif current_price[-1:] == 'b':
			current_price = float(current_price[0:-1]) * 1000000000
		self.Current_price = int(current_price)
		
		self.Today_trend = today_trend
		today_price = str(today_price)
		today_price = today_price.replace(',','')
		today_price = today_price.replace(' ','')
		if today_price[-1:] == 'm':
			today_price = float(today_price[0:-1]) * 1000000
		elif today_price[-1:] == 'k':
			today_price = float(today_price[0:-1]) * 1000
		elif today_price[-1:] == 'b':
			today_price = float(today_price[0:-1]) * 1000000000
		self.Today_price = today_price

	
		