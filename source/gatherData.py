import json
import requests
import sqlite3
from Item import *


def run():
	
	url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=21787'
	data2 = requests.get(url)
	data2 = data2.json()
	print (json.dumps(data2,indent = 4))
	data2 = data2['item']
	
	icon = data2['icon']
	icon_large = data2['icon_large']
	type  = data2['type']
	name = data2['name']
	description = data2['description']
	members = data2['members']
	price = data2['current']['price']
	current = data2['current']
	today = data2['today']
	day30 = data2['day30']
	day90 = data2['day90']
	day180 = data2['day180']
	
	item_Record = Item(icon,icon_large,type,name,description,members,price,current,today,day30,day90,day180)
	
	con = sqlite3.connect("GE_Data.db")
	cur = con.cursor()
	cur.execute('''create table if not exists item_Record(Icon text, Icon_Large text, Type text ,Name text,
				Description text, Members bool, Price int, Current text[], 
				Today text[], Day30 text[], Day90 text[], Day180 text[] )''')
				
	sqltest = "INSERT INTO item_Record VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
	cur.execute(sqltest,(item_Record.Icon,item_Record.Icon_large,item_Record.Type,item_Record.Name,item_Record.Description,item_Record.Members,item_Record.Price,item_Record.Current,item_Record.Today,item_Record.Day30,item_Record.Day90,item_Record.Day180))
	#sqlCmd = ''' insert into item_Record 
			#('Icon','icon_Large','Type,Name','Description','Members',
			#'Trend','Price','Change','Current','Today','Day30','Day90','Day180') 
			#''') 
			
#sql1 = "Select item_Record from GE_Data"
#print(con.query(sql1))
	
	#data2 = json.loads(data2)
	#item = json.dumps(data2,indent = 4)
	#print(item)
#cur.execute('''
			#insert into item_Record 
			#('Icon','icon_Large','Type,Name','Description','Members',
			#'Trend','Price','Change','Current','Today','Day30','Day90','Day180') 
			#VALUES
			#()
			#''')
#cur.execute('''insert into item_Record ('Name') VALUES(Name)''')
				
#sql = "CREATE DATABASE IF NOT EXISTS GE_Data"
#db1.execute(sql)
#con = sqlite3.connect("GE_Data.db")
#cur = con.cursor()
#cur.execute("create table TopIndianListners(Artist text, Listeners text)")
