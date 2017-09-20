import json
import requests
import sqlite3
import time
from Item import *


def run(url):
	#url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=21787'
	data = requests.get(url)
	time.sleep(.01)
	if(data.status_code == 404):
		print('Item Doesnt Exist.')
		return
	r = requests.post(url,data)
	r.connection.close()
	if r:
		data = data.json()
		#data = json.loads(data)
		print (str(json.dumps(data,indent = 4)))
		data = data['item']
		
		icon = data['icon']
		icon_large = data['icon_large']
		id = int(data['id'])
		type  = data['type']
		name = data['name']
		description = data['description']
		members = data['members']

		current_trend = data['current']['trend']
		current_price = data['current']['price']
		today_trend = data['today']['trend']
		today_price = data['today']['price']
		day30_trend = data['day30']['trend']
		day30_change = data['day30']['change']
		day90_trend = data['day90']['trend']
		day90_change = data['day90']['change']
		day180_trend = data['day180']['trend']
		day180_change = data['day180']['change']
		
		item_Record = Item(icon, icon_large,id,type, name, description, members, current_trend,current_price,today_trend,today_price,day30_trend,day30_change,day90_trend,day90_change,day180_trend,day180_change)
						
		con = sqlite3.connect("GE_Data.db")
		cur = con.cursor()
		cur.execute('''create table if not exists item_Record(Icon text, Icon_Large text,Id int, Type text ,Name text,
					Description text, Members bool, Current_trend text, Current_price int, Today_trend text, Today_price text,
					Day30_trend text, Day30_change text, Day90_trend text, Day90_change text, Day180_trend text, Day180_change text)''')
				
		sqlq = "SELECT COUNT(1) FROM item_Record WHERE Id = ?"
		cur.execute(sqlq,(id,))
		if not cur.fetchone()[0]:
			sql = "INSERT INTO item_Record VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
			cur.execute(sql,(item_Record.Icon,item_Record.Icon_large,item_Record.Id,item_Record.Type,item_Record.Name,item_Record.Description,item_Record.Members,item_Record.Current_trend,item_Record.Current_price,item_Record.Today_trend,item_Record.Today_price,item_Record.Day30_trend,item_Record.Day30_change,item_Record.Day90_trend,item_Record.Day90_change,item_Record.Day180_trend,item_Record.Day180_change))
			con.commit()
		else:
			print('Record already exists.')
		cur.close()
		con.close()