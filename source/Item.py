class Item():
	Icon = ''
	Icon_large = ''
	Type = '' 
	Name = ''
	Description = ''
	Members = False
	Price = 0
	Current = []
	Today = []
	Day30 = []
	Day90 = []
	Day180 = [] 
	
	def __init__(self, icon, icon_large, type, name, description, members, price, current, today, day30, day90, day180):
		self.Icon = icon
		self.Icon_large = icon_large
		self.Type = type
		self.Name = name
		self.Description = description
		if members == 'true':
			members = True
		else:
			members = False
		self.Members = members
		if price[-1:] == 'm':
			price = float(price[0:-1]) * 1000000
		else:
			price = float(price[0:-1]) * 1000
		self.Price = int(price)
		self.Current = current
		self.Today = today
		self.Day30 = day30
		self.Day90 = day90
		self.Day180 = day180
		
	def Item(self, icon, icon_large, type, name, description, members, price, current, today, day30, day90, day180):
		self.Icon = icon
		self.Icon_large = icon_large
		self.Type = type
		self.Name = name
		self.Description = description
		if members == 'true':
			members = True
		else:
			members = False
		self.Members = members
		if price[-1:] == 'm':
			price = float(price[0:-1]) * 1000000
		else:
			price = float(price[0:-1]) * 1000
		self.Price = int(price)
		self.Current = current
		self.Today = today
		self.Day30 = day30
		self.Day90 = day90
		self.Day180 = day180
	
		