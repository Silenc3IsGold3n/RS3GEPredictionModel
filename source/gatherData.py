import json
import requests
import sqlite3
from Item import *


def run(url):
	
	#url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=21787'
	data2 = requests.get(url)
	if(data2):
		data2 = data2.json()
		print (json.dumps(data2,indent = 4))
		data2 = data2['item']
		
		icon = data2['icon']
		icon_large = data2['icon_large']
		type  = data2['type']
		name = data2['name']
		description = data2['description']
		members = data2['members']

		current_trend = data2['current']['trend']
		current_price = data2['current']['price']
		today_trend = data2['today']['trend']
		today_price = data2['today']['price']
		day30_trend = data2['day30']['trend']
		day30_change = data2['day30']['change']
		day90_trend = data2['day90']['trend']
		day90_change = data2['day90']['change']
		day180_trend = data2['day180']['trend']
		day180_change = data2['day180']['change']
		
		item_Record = Item(icon, icon_large, type, name, description, members, current_trend,current_price,today_trend,today_price,day30_trend,day30_change,day90_trend,day90_change,day180_trend,day180_change)
						
		con = sqlite3.connect("GE_Data.db")
		cur = con.cursor()
		cur.execute('''create table if not exists item_Record(Icon text, Icon_Large text, Type text ,Name text,
					Description text, Members bool, Current_trend text, Current_price int, Today_trend text, Today_price text,
					Day30_trend text, Day30_change text, Day90_trend text, Day90_change text, Day180_trend text, Day180_change text)''')
					
		sqltest = "INSERT INTO item_Record VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
		cur.execute(sqltest,(item_Record.Icon,item_Record.Icon_large,item_Record.Type,item_Record.Name,item_Record.Description,item_Record.Members,item_Record.Current_trend,item_Record.Current_price,item_Record.Today_trend,item_Record.Today_price,item_Record.Day30_trend,item_Record.Day30_change,item_Record.Day90_trend,item_Record.Day90_change,item_Record.Day180_trend,item_Record.Day180_change))


	#sql1 = "Select * from item_Record"
	#cur.execute(sql1)
	#row = cur.fetchall()
	#for i in row:
		#print(str(i) + '\n')
	
	
	
	