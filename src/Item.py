class Item():
	Icon = ''
	Icon_large = ''
	Id = 0
	Type = '' 
	Name = ''
	Description = ''
	Members = False
	Current_trend = ''
	Current_price = 0
	Today_trend = ''
	Today_price = ''
	Day30_trend = ''
	Day30_change = ''
	Day90_trend = ''
	Day90_change = ''
	Day180_trend = ''
	Day180_change = ''
	
	def __init__(self, icon, icon_large,id,type, name, description, members, current_trend,current_price,today_trend,today_price,day30_trend,day30_change,day90_trend,day90_change,day180_trend,day180_change):
		self.Icon = icon
		self.Icon_large = icon_large
		self.Id = id
		self.Type = type
		self.Name = name
		self.Description = description
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
		self.Today_price = today_price
		self.Day30_trend = day30_trend
		self.Day30_change = day30_change
		self.Day90_trend = day90_trend
		self.Day90_change = day90_change
		self.Day180_trend = day180_trend
		self.Day180_change = day180_change
	
		